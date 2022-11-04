import streamlit as st
import pandas as pd
import altair as alt
import pandas.io.sql as sqlio
import numpy as np
from src.database.logics import PostgresConnector
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> col_name (str): Name of the column (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (mandatory)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> col_mean (int): Average value of a serie (optional)
    -> col_std (int): Standard deviation value of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> col_median (int): Median value of a serie (optional)
    -> n_zeros (int): Number of times a serie has values equal to 0 (optional)
    -> n_negatives (int): Number of times a serie has negative values (optional)
    -> histogram (int): Altair histogram displaying the count for each bin value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)
    """

    def __init__(self,table_name='order_details',col_name='discount'):
            self.table_name=table_name
            self.col_name=col_name
            self.db=PostgresConnector()
            self.schema_name =self.db.database
            self.serie=None
            self.n_unique=None
            self.n_missing=None
            self.col_mean=None
            self.col_std=None
            self.col_min=None
            self.col_max=None
            self.col_median=None
            self.n_zeros=None
            self.n_negatives=None
            self.histogram=None
            self.frequent=None

    
    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Use pandas.sql.io to read sql into a dataframe
        -> Extract the particular column and store in serie variable in the form of pandas series
        --------------------
        Returns
        --------------------
        -> None
        """
        self.serie = sqlio.read_sql_query('select {} from {}'.format(self.col_name,self.table_name), self.db.conn)[self.col_name]

        
    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Check if the type of serie variable is equal to the type of pandas series
        --------------------
        Returns
        --------------------
        output (bool) : Boolean for whether serie variable is None or of type pandas series
        """
        return str(type(self.serie))!="<class 'pandas.core.series.Series'>"
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column using a SQL query (get_unique_query())
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Get the sql query from get_unique_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe
        -> Set the value of n_unique as this dataframe's first element
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_unique_query(self.db.database,self.table_name,self.col_name)
        self.n_unique=sqlio.read_sql_query(sql,self.db.conn)['count'][0]

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of n_missing as the length of serie where value of serie is null
        --------------------
        Returns
        --------------------
        None
        """
        self.n_missing=len(self.serie[self.serie==np.nan])

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of n_zeros as the length of serie where value of serie is zero
        --------------------
        Returns
        --------------------
        None
        """
        self.n_zeros=len(self.serie[self.serie==0])

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values using a SQL query (get_negative_number_query())
        --------------------
        Parameters
        --------------------
        No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Get the sql query from get_negative_number_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe
        -> Set the value of n_negatives as as this dataframe's first element
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_negative_number_query(self.db.database,self.table_name,self.col_name)
        self.n_negatives=sqlio.read_sql_query(sql,self.db.conn)['count'][0]

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of col_mean as the mean of serie
        --------------------
        Returns
        --------------------
        None
        """
        self.col_mean=self.serie.mean()

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie using a SQL query (get_std_query)

        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Get the sql query from get_std_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe
        -> Set the value of col_std as as this dataframe's first element
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_std_query(self.db.database,self.table_name,self.col_name)
        self.col_std=sqlio.read_sql_query(sql,self.db.conn)['stddev'][0]

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of col_min as the minimum value of serie
        --------------------
        Returns
        --------------------
        None
        """
        self.col_min=self.serie.min()

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of col_min as the maximum value of serie
        --------------------
        Returns
        --------------------
        None
        """
        self.col_max=self.serie.max()

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie
        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of col_median as the median value of serie
        --------------------
        Returns
        --------------------
        None
        """
        self.col_median=self.serie.median()

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie
        --------------------
        Parameters
        --------------------
        ->No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Store the Altair histogram displaying the count for each bin value of a serie
        --------------------
        Returns
        --------------------
        None
        """
        self.histogram=alt.Chart(pd.DataFrame(self.serie)).mark_bar().encode(x = self.col_name,
                                             y = 'count()')

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie
        --------------------
        Parameters
        --------------------
        -> end (int) : THreshold of frequency
        --------------------
        Pseudo-Code
        --------------------
        -> Calculate the most frequent value of serie
        -> Storing the dataframe of the most frequent value
        --------------------
        Returns
        --------------------
        None
        """
        self.frequent=pd.DataFrame([self.serie.value_counts().index[0]],columns=['Most Frequent Value'])

    def get_summary_df(self,):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value
        --------------------
        Parameters
        --------------------
        No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Call all the class functions to initilize the class attributes and create the dictionary of all the variables
        -> Convert this dictionary into a dataframe object
        -> Use the streamlit's dataframe function to display the ouput in the streamlit application
        --------------------
        Returns
        --------------------
        None
        """
        
        self.db.open_connection()
        self.set_data()
        self.set_unique()
        self.set_missing()
        self.set_zeros()
        self.set_negatives()
        self.set_mean()
        self.set_std()
        self.set_min()
        self.set_max()
        self.set_median()
        dict_df={('Number of unique value of a serie',self.n_unique),
                    ('Number of missing values of a serie',self.n_missing),
                    ('Average value of a serie',self.col_mean),
                    ('Standard deviation value of a serie',self.col_std),
                    ('Minimum value of a serie',self.col_min),
                    ('Maximum value of a serie',self.col_max),
                    ('Median value of a serie',self.col_median),
                    ('Number of times a serie has values equal to 0',self.n_zeros),
                    ('Number of times a serie has negative values',self.n_negatives)}
        df=pd.DataFrame(dict_df,columns=['Description','Value'])
        st.dataframe(df)
        self.db.close_connection()
        return dict_df


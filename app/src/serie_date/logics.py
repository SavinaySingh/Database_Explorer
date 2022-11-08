import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_date.queries import get_min_date_query, get_weekend_count_query, get_1900_count_query

class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column loaded from Postgres

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
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.table_name=table_name
        self.col_name=col_name
        self.db=PostgresConnector()
        self.schema_name = self.db.database
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_min = None
        self.col_max = None
        self.n_weekend = None
        self.n_weekday = None
        self.n_future = None
        self.n_empty_1900 = None
        self.n_empty_1970 = None
        self.n_barchart = None
        self.n_frequent = None
        

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

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
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of n_unique as this dataframe's first element
        --------------------
        Returns
        --------------------
        None
        """
        self.n_unique = self.serie.nunique 
        
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

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie using a SQL query (get_min_date_query())

        --------------------
        Parameters
        --------------------
        -> Get the sql query from get_min_date_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe and seet the value of self.col_min
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_min_date_query(self.db.database,self.table_name,self.col_name)
        self.col_min=sqlio.read_sql_query(sql,self.db.conn)


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
        -> Set the value of col_max as the max of serie
        --------------------
        Returns
        --------------------
        None
        """
        self.col_max=self.serie.max()
        
    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend using a SQL query (get_weekend_count_query())
        
        --------------------
        Parameters
        --------------------
        -> Get the sql query from get_weekend_count_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe and seet the value of self.n_weekend
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_weekend_count_query(self.db.database,self.table_name,self.col_name)
        self.n_weekend=sqlio.read_sql_query(sql,self.db.conn)

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend

        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of self.n_weekday
        --------------------
        Returns
        --------------------
        None

        """
        self.n_weekday = len(self.serie[self.serie.dt.dayofweek])

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future

        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of n_future
        --------------------
        Returns
        --------------------
        None
        """
        self.n_future = len(self.serie(pd.to_datetime("today").strftime("%m/%d/%Y")))

    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' using a SQL query (get_1900_count_query())

        --------------------
        Parameters
        --------------------
        -> Get the sql query from get_1900_count_query function from queries file
        -> Use pandas.sql.io to read this SQL query into a dataframe and seet the value of self.n_empty_1900
        --------------------
        Returns
        --------------------
        None
        """
        sql=get_1900_count_query(self.db.database,self.table_name,self.col_name)
        self.n_empty_1900=sqlio.read_sql_query(sql,self.db.conn)

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has dates equal to '1970-01-01'

        --------------------
        Parameters
        --------------------
        -> No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Set the value of n_empty_1970
        --------------------
        Returns
        --------------------
        None

        """
        self.n_empty_1970 = len(self.serie.isin([''1970-01-01']))
`        
    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        ->No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Store the Altair barchart displaying the count for each value of a serie
        --------------------
        Returns
        --------------------

        """
        self.n_barchart = alt.Chart(source).mark_bar().encode(x = self.col_name,y = 'count()')
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        => To be filled by student

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        => To be filled by student

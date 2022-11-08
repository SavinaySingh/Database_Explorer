import pandas as pd
import streamlit as st

from src.database.logics import PostgresConnector
from src.dataframe.queries import get_numeric_tables_query, get_text_tables_query, get_date_tables_query


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> df (pd.Dataframe): Pandas dataframe where the table content has been loaded (mandatory)
    -> n_rows (int): Number of rows of dataset (optional)
    -> n_cols (int): Number of columns of dataset (optional)
    -> n_duplicates (int): Number of duplicated rows of dataset (optional)
    -> n_missing (int): Number of missing values of dataset (optional)
    -> num_cols (list): List of columns of numerical type (optional)
    -> text_cols (list): List of columns of text type (optional)
    -> date_cols (list): List of columns of datetime type (optional)
    """
    def __init__(self, schema_name='public', table_name='order_details', db=None, df=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.db = PostgresConnector()
        self.df = df
        self.n_rows = None
        self.n_cols= None
        self.n_duplicates = None
        self.n_missing = None
        self.num_cols = None
        self.text_cols = None
        self.date_cols = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Overall section of Streamlit app 

        --------------------
        Parameters
        --------------------
        No Parameters

        --------------------
        Pseudo-Code
        --------------------


        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        self.df = sqlio.read_sql_query('select {} from {}'.format(self.col_name,self.table_name), self.db.conn)[self.col_name]

        
    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        self.df = the dataframe to check if it is emptry or none

        --------------------
        Pseudo-Code
        --------------------
        if df is empty:
            return True
        else:
            return False

        --------------------
        Returns
        --------------------
        True : Boolean
        False : Boolean

        """
        if(self.df.empty):
            return True
        else:
            return False

    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df and store them as attributes (self.n_rows, self.n_cols)

        --------------------
        Parameters
        --------------------
        self.df = the dataframe to compute dimensions

        --------------------
        Pseudo-Code
        --------------------
        n_rows = length(df.axes[0]) #Here axes[0] refers to rows
        n_cols = length(df.axes[1]) #Here axes[1] refers to cols

        --------------------
        Returns
        --------------------
        returns a print statement

        """
        self.n_rows = len(df.axes[0])
        self.n_cols = len(df.axes[1])
        
        #print('The number of rows are',self.n_rows)
        #print('The number of columns are',self.n_cols)
        
    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store it as attribute (self.n_duplicates)

        --------------------
        Parameters
        --------------------
        self.df = the dataframe to compute duplicated values

        --------------------
        Pseudo-Code
        --------------------
        n_duplicates = df[df.duplicated()] #The duplicated() checks the dataframe for duplicate values

        --------------------
        Returns
        --------------------
        returns n_duplicates of type object

        """
        self.n_duplicates = df[df.duplicated()]
        
        return self.n_duplicates
    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store it as attribute (self.n_missing)

        --------------------
        Parameters
        --------------------
        
        self.df = the dataframe to compute missing values

        --------------------
        Pseudo-Code
        --------------------
        n_missing = df.isna().sum().sum() #Here isna() checks for missing values in df and then sum() calculates the number of missing values

        --------------------
        Returns
        --------------------
        returns self.n_missing

        """
        self.n_missing = df.isna().sum().sum()
    
        return self.n_missing
    
    def set_numeric_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric_columns (method): Class method that extract the list of numeric columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.num_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Gets the sql query from get_numeric_table_query and stores it in sql variable
        -> Use pandas.sql.io to read the query into a dataframe and sets the value of self.num_cols
        --------------------
        Returns
        --------------------
        None
        
        """
        sql = get_numeric_table_query(self.schema_name,self.table_name)
        self.num_cols = sqlio.read_sql_query(sql,self.db.conn)
        

    def set_text_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_text_columns (method): Class method that extract the list of text columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.text_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Gets the sql query from get_text_table_query and stores it in sql variable
        -> Use pandas.sql.io to read the query into a dataframe and sets the value of self.text_cols
        
        --------------------
        Returns
        --------------------
        None
        
        """
        sql = get_text_table_query(self.schema_name,self.table_name)
        self.num_cols = sqlio.read_sql_query(sql,self.db.conn)
        
        
    def set_date_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_date_columns (method): Class method that extract the list of datetime columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.date_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        None
        --------------------
        Pseudo-Code
        --------------------
        -> Gets the sql query from get_date_table_query and stores it in sql variable
        -> Use pandas.sql.io to read the query into a dataframe and sets the value of self.text_cols
        
        --------------------
        Returns
        --------------------
        None
        """
        sql = get_date_table_query(self.schema_name,self.table_name)
        self.num_cols = sqlio.read_sql_query(sql,self.db.conn)
        
    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        
        self.df = the dataframe to compute the first rows
        n = number of rows
        
        --------------------
        Pseudo-Code
        --------------------
        
        return df.first(n) #Here first returns the rows from the top of the dataframe

        --------------------
        Returns
        --------------------
        returns the first 5 rows of the dataframe of type object
        """
        return self.df.head(n)

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        
        self.df = the dataframe to compute the last rows
        n = number of rows
        
        --------------------
        Pseudo-Code
        --------------------
        
        return df.tail(n) #Here tail returns the rows from the bottom of the dataframe

        --------------------
        Returns
        --------------------
        returns the last 5 rows of the dataframe of type object

        """
        return self.df.tail(n)

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        
        self.df = the dataframe to compute random sample of rows
        n = number of rows

        --------------------
        Pseudo-Code
        --------------------
        
        return df.sample(n=n) #here sample() selects random rows and columns from a dataframe

        --------------------
        Returns
        --------------------
        
        returns 5 random rows from the dataframe of type object

        """
        return self.df.sample(n=n)

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        No Parameters
        --------------------
        Pseudo-Code
        --------------------
        -> Calls all the class functions to initialize the class attributes and create the dictionary of all the variables
        -> Convert this dictionary into a dataframe object
        -> Use the streamlit's dataframe function to display the ouput in the streamlit application

        --------------------
        Returns
        --------------------
        None
        
        """
        self.db.open_connection()
        self.set_data()
        self.is_df_none()
        self.set_dimensions()
        self.set_duplicates()
        self.set_missing()
        self.set_numeric_columns()
        self.set_text_columns()
        self.set_date_columns()
        self.get_head()
        self.get_tail()
        self.get_sample()
        dict = {('Number of rows and columns are',(self.n_rows,self.n_cols)),
                ('Number of duplicated rows of dataset are',self.n_duplicates),
                ('Number of missing values in the dataset are',self.n_missing),
                ('List of columns of numeric type are',self.num_cols),
                ('List of columns of text type are',self.text_cols),
                ('List of columns of date type are',self.date_cols)}
        df=pd.DataFrame(dict_df,columns=['Description','Value'])
        st.dataframe(df)
        self.db.close_connection()
        return dict_df
        

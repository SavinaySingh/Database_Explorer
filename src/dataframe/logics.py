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
    def __init__(self, schema_name=None, table_name=None, db=None, df=None):
        => To be filled by student

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Overall section of Streamlit app 

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
        
        print('The number of rows are',self.n_rows)
        print('The number of columns are',self.n_cols)
        
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
        #database connection
        
        cur = conn.cursor()
        # execute a statement

        cur.execute(get_numeric_tables_query(self))
        
        self.num_cols = cur.fetchall()
        
        

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
        #database connection
        
        cur = conn.cursor()
        # execute a statement

        cur.execute(get_text_tables_query('public','categories')(self))
        
        self.num_cols = cur.fetchall()

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
        #database connection
        
        cur = conn.cursor()
        # execute a statement

        cur.execute(get_date_tables_query(self))
        
        self.num_cols = cur.fetchall()

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

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
        return df.head(n)

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5)

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
        return df.tail(n)

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5)

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
        return df.sample(n=n)

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

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

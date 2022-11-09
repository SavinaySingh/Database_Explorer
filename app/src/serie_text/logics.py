from cmath import isnan
from queue import Empty
import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_text.queries import get_missing_query, get_mode_query, get_alpha_query

class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column loaded from Postgres

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
    -> n_empty (int): Number of times a serie has empty value (optional)
    -> n_mode (int): Mode value of a serie (optional)
    -> n_space (int): Number of times a serie has only space characters (optional)
    -> n_lower (int): Number of times a serie has only lowercase characters (optional)
    -> n_upper (int): Number of times a serie has only uppercase characters (optional)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (optional)
    -> n_digit (int): Number of times a serie has only digit characters (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie 
    
    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Text section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        -> use st.table function to display all relevent infomation in a table format in the Text section of Streamlit app

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return st.table({'Description':['Number of unique values','Number of rows with missing values','Number of empty rows','Number of rows with only whitespace','Number of rows with only lowercases','Number of rows with only uppercases','Number of rows with only Alphabet','Number of rows with only digits','Mode value'],'Value':[self.set_unique(),self.set_missing(),self.set_empty(),self.set_whitespace(),self.set_lowercase(),self.set_uppercase(),self.set_alphabet(),self.set_digit(),self.set_mode()]})
      
    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded

        --------------------
        Pseudo-Code
        --------------------
        -> use if else statement to check if the series is empty or not, if its empty print the total number of empty cells.
        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        if self.serie.isnull().sum() > 0:
            return self.serie.isnull().sum()
        elif self.serie.isna().sum() == 0:
            return self.serie.isna().sum()
        elif self.serie.isna().sum() >0:
            return self.serie.isna().sum()
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded

        --------------------
        Pseudo-Code
        --------------------
        -> use nunique() function of python to computes the number of unique value of a serie

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.serie.nunique()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie using a SQL query (get_missing_query())

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded
        schema_name (str): Name of the dataset schema 
        table_name (str): Name of the dataset table 

        --------------------
        Pseudo-Code
        --------------------
        -> use sql query (get_missing_query()) from queries.py file to compute the number of missing value

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.db.run_query(get_missing_query(schema_name, table_name, serie))

    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded

        --------------------
        Pseudo-Code
        --------------------
        -> use isna().sum() of python on self.serie

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.serie.isna().sum()

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie using a SQL query (get_mode_query())

        --------------------
        Parameters
        --------------------
        schema_name (str): Name of the dataset schema 
        table_name (str): Name of the dataset table
        col_name (str): Name of the column 

        --------------------
        Pseudo-Code
        --------------------
        -> use sql query (get_mode_query()) from queries.py file to compute the mode value of a serie
        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.db.run_query(get_mode_query(self.schema_name, self.table_name, self.col_name)) 

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded

        --------------------
        Pseudo-Code
        --------------------
        -> use str.isspace().sum() python function to compute the number of times a serie has only space characters

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.serie.str.isspace().sum() 
        #https://stackoverflow.com/questions/72477286/count-number-of-consecutive-spaces-in-series
        #https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isspace.html


    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters

        --------------------
        Parameters
        --------------------
        serie (pd.Series): Pandas serie where the content of a column has been loaded

        --------------------
        Pseudo-Code
        --------------------
        -> use str.islower().sum() python function to compute the number of times a serie has only lowercase characters

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.serie.str.islower().sum()

    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters

        -------------------- 
        Parameters
        --------------------
        => To be filled by student
        serie (pd.Series): Pandas serie where the content of a column has been loaded

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
        return self.serie.str.isupper().sum()
    
    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters using a SQL query (get_alpha_query())

        --------------------
        Parameters
        --------------------
        => To be filled by student
        schema_name (str): Name of the dataset schema 
        table_name (str): Name of the dataset table
        col_name (str): Name of the column 

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
        return self.db.run_query(get_alpha_query(self.schema_name, self.table_name, self.col_name))

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters

        --------------------
        Parameters
        --------------------
        => To be filled by student
        serie (pd.Series): Pandas serie where the content of a column has been loaded
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
        return self.serie.str.isdigit().sum()

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        => To be filled by student
        serie (pd.Series): Pandas serie where the content of a column has been loaded

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
        df = self.serie.to_frame()
        data = alt.Chart(df).mark_bar().encode( x='index', y=0)
        st.altair_chart(data, use_container_width=True)
      
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
        serie (pd.Series): Pandas serie where the content of a column has been loaded

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
        countfreq = self.serie.value_counts()
        countfreq = countfreq.to_frame()
        st.dataframe(countfreq.head(end))

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
        return st.table({'Description':['Number of unique values','Number of rows with missing values','Number of empty rows','Number of rows with only whitespace','Number of rows with only lowercases','Number of rows with only uppercases','Number of rows with only Alphabet','Number of rows with only digits','Mode value'],'Value':[self.set_unique(),self.set_missing(),self.set_empty(),self.set_whitespace(),self.set_lowercase(),self.set_uppercase(),self.set_alphabet(),self.set_digit(),self.set_mode()]})

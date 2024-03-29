import streamlit as st

from src.serie_date.logics import DateColumn
from src.database.logics import PostgresConnector
import pandas.io.sql as 

def display_dates():
    """
    --------------------
    Description
    --------------------
    -> display_dates (function): Function that displays all the relevant information for every datetime column of a table

    --------------------
    Parameters
    --------------------
    -> No parameters
    --------------------
    Pseudo-Code
    --------------------
    -> Create the sql query to select all the rows and columns from the table
    -> Use pandas.sql.io to store these rows into a dataframe
    -> Filter this dataframe to only store numeric columns
    -> For each numerical column run get_summary_df function of DateColumn class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None
    """
    table_name='order_details'
    sql='select * from {}'.format(table_name)
    dat = sqlio.read_sql_query(sql, db.conn)
    date_var= ['datetime64','timestamp without time zone','timestamp with time zone','time with time zone','time without time zone','interval', 'date']
    df = dat.select_dtypes(include=date_var)
    date_cols=list(df.columns)
    for cols in datecols_cols:
        numeric=DateColumn(table_name='order_details',col_name=cols)
        numeric.get_summary_df()

def display_date(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_date (function): Function that instantiates a DateColumn class from a dataframe column and displays all the relevant information for a single datetime column of a table

    --------------------
    Parameters
    --------------------
    -> No parameter
    --------------------
    Pseudo-Code
    --------------------
    -> Initialize the DateColumn class object with one particular column
    -> Run get_summary_df function of DateColumn class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None
    """
    date_var=DateColumn(table_name='order_details',col_name=col_name)
    date_var.get_summary_df()

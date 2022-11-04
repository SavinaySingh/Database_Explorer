import streamlit as st

from src.serie_numeric.logics import NumericColumn
from src.database.logics import PostgresConnector
import pandas.io.sql as sqlio

db=PostgresConnector()
db.open_connection()
def display_numerics():
    """
    --------------------
    Description
    --------------------
    -> display_numerics (function): Function that displays all the relevant information for every numerical column of a table

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
    -> For each numerical column run get_summary_df function of NumericColumn class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None
    """
    table_name='order_details'
    sql='select * from {}'.format(table_name)
    dat = sqlio.read_sql_query(sql, db.conn)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = dat.select_dtypes(include=numerics)
    numeric_cols=list(newdf.columns)
    for cols in numeric_cols:
        numeric=NumericColumn(table_name='order_details',col_name=cols)
        numeric.get_summary_df()
    
    

def display_numeric(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_numeric (function): Function that instantiates a NumericColumn class from a dataframe column and displays all the relevant information for a single numerical column of a table

    --------------------
    Parameters
    --------------------
    -> No parameter
    --------------------
    Pseudo-Code
    --------------------
    -> Initialize the NumericColumn class object with one particular column
    -> Run get_summary_df function of NumericColumn class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None
    """
    numeric=NumericColumn(table_name='order_details',col_name=col_name)
    numeric.get_summary_df()

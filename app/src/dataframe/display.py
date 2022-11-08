import streamlit as st

from src.dataframe.logics import Dataset

def read_data():
    """
    --------------------
    Description
    --------------------
    -> read_data (function): Function that loads the content of the Postgres table selected, extract its schema information and instantiate a Dataset class accordingly

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

def display_overall():
    """
    --------------------
    Description
    --------------------
    -> display_overall (function): Function that displays all the information on the Overall section of the streamlit app

    --------------------
    Parameters
    --------------------
    -> No parameter
    --------------------
    Pseudo-Code
    --------------------
    -> Initialize the Dataset class object with one particular column
    -> Run get_summary_df function of Dataset class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None

    """
    overall = Dataset(schema_name='public',table_name='order_details',col_name=col_name)
    overall.get_summary_df()

def display_dataframes():
    """
    --------------------
    Description
    --------------------
    -> display_dataframes (function): Function that displays all the information on the Explore section of the streamlit app

    --------------------
    Parameters
    --------------------
    -> No parameter
    --------------------
    Pseudo-Code
    --------------------
    -> Initialize the Dataset class object with one particular column
    -> Run get_summary_df function of Dataset class to set the values of class attributes
    -> Display the output in Streamlit application
    --------------------
    Returns
    --------------------
    None

    """
    explore = Dataset(schema_name='public',table_name='order_details',col_name=col_name)
    explore.get_summary_df()

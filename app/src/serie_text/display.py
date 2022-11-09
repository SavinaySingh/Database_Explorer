import streamlit as st

from src.serie_text.logics import TextColumn

def display_texts(table_name, schema_name):
    """
    --------------------
    Description
    --------------------
    -> display_texts (function): Function that displays all the relevant information for every text column of a table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of the dataset schema 
    -> table_name (str): Name of the dataset table 

    --------------------
    Pseudo-Code
    --------------------
    
    load data -> convert data into dataframe -> select data having data type as string-> make a list of columns-> itterate through the list of columns-> expand each column and display relevent information for every text column

    --------------------
    Returns
    --------------------

    -> (type): description

    """
    load_data = st.session_state.db.load_table(table_name, schema_name)
    dataset = pd.DataFrame(load_data)
    dataset = dataset.convert_dtypes().dtypes
    dataset = dataset.loc[data['datatype']=='string']
    col_list = list(data['index'])
    count = 1
    for name in col_list:
        with st.expander(f"{count}. Column: {str(name)}", expanded=False):
            col_serie = st.session_state.db.run_query(f"SELECT {name} FROM {schema_name}.{table_name};")
            display_text(table_name, schema_name, name, col_serie)
            count = count+1

def display_text(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_text (function): Function that instantiates a TextColumn class from a dataframe column and displays all the relevant information for a single text column of a table

    --------------------
    Parameters
    --------------------

    -> schema_name (str): Name of the dataset schema 
    -> table_name (str): Name of the dataset table
    -> col_name (str): Name of the column

    --------------------
    Pseudo-Code
    --------------------
    -> use TextColumn class and give information about db,schema_name,table_name,col_name and serie and use set_data method to display all information of the column.
    --------------------
    Returns
    --------------------
    -> (type): description

    """
    disp_text = TextColumn(db=st.session_state.db, schema_name=schema_name, table_name=table_name, col_name=col_name,  serie = pd.Series(i))
    disp_text.set_data()

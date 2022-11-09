import streamlit as st
import pandas as pd
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
    '''As the student B was unable to complete the config file, I have set the session_state within this function. In order to run my part, the following steps needs to be taken:
    1. In logics.py change "from queries import get_tables_list_query, get_table_data_query, get_table_schema_query" to "from src.database.queries import get_tables_list_query, get_table_data_query, get_table_schema_query"
    2. Comment out the incomplete function run_query(self, sql_query)
    3. Comment out the expander in the open_connection() in logics.py as it will lead to nested expanders '''
    if 'table_selected' not in st.session_state:
        st.session_state['table_selected'] = 'order_details'
    if 'schema_selected' not in st.session_state:
        st.session_state['schema_selected'] = 'public'
    table_name=st.session_state['table_selected']
    schema_name=st.session_state['schema_selected']
    sql='select * from {}.{}'.format(schema_name,table_name)
    dat = sqlio.read_sql_query(sql, db.conn)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = dat.select_dtypes(include=numerics)
    numeric_cols=list(newdf.columns)
    for cols in numeric_cols:
        with st.expander(f'{cols}'):
            numeric=NumericColumn(schema_name,table_name=table_name,col_name=cols)
            dict_df=numeric.get_summary_df()
            numeric.set_histogram()
            st.altair_chart(numeric.histogram, use_container_width=True)
            df=sqlio.read_sql_query('select {} from {}.{}'.format(cols,schema_name,table_name), db.conn)
            df_freq=pd.DataFrame(df.value_counts().index,columns=['value'])
            df_freq['occurence']=df.value_counts().values
            df_freq['percentage']=[(x/sum(df_freq['occurence']))*100 for x in df.value_counts().values]
            st.dataframe(df_freq)

    

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
    if 'table_selected' not in st.session_state:
        st.session_state['table_selected'] = 'order_details'
    if 'schema_selected' not in st.session_state:
        st.session_state['schema_selected'] = 'public'
    table_name=st.session_state['table_selected']
    schema_name=st.session_state['schema_selected']
    numeric=NumericColumn(table_name='order_details',col_name=col_name)
    numeric.get_summary_df()
    numeric.set_histogram()
    st.altair_chart(numeric.histogram, use_container_width=True)
    df=sqlio.read_sql_query('select {} from {}.{}'.format(col_name,schema_name,table_name), db.conn)
    df_freq=pd.DataFrame(df.value_counts().index,columns=['value'])
    df_freq['occurence']=df.value_counts().values
    df_freq['percentage']=[(x/sum(df_freq['occurence']))*100 for x in df.value_counts().values]
    st.dataframe(df_freq)
 

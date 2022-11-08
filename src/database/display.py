import streamlit as st
from src.database.logics import PostgresConnector
def display_db_connection_menu():
    P = PostgresConnector()
    """
    --------------------
    Description
    --------------------
    -> display_db_connection_menu (function): Function that displays the menu for connecting to a database and triggers the database connection

    --------------------
    Parameters
    --------------------
    => User Name , Password, Database Host , Database port 
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => the form is prefilled by the parameters to connect the database and 
    connect to submit the form by validating the creditials
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => prefilled form with the connect credentials
    -> (type): description

    """
    st.header('Streamlit application for performing data exploration on a database')
    st.title('Database connection details')
    with st.form(key='databaseconnect'):
        st.text_input(label="User Name", value=P.user)
        st.text_input(label="Password", type="password",value = P.password)
        st.text_input(label="DataBase Host",value=P.host)
        st.text_input(label="DataBase Name", value=P.database)
        st.text_input(label="DataBase Port", value=P.port)
        submit_button = st.form_submit_button(label='Connect')
        if submit_button:
            connect_db()
def connect_db():
    """
    --------------------
    Description
    --------------------
    -> connect_db (function): Function that connects to a database and instantiate a PostgresConnector class accordingly

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

    P1 = PostgresConnector()
    P1.open_connection()
    P1.open_cursor()
    P1.list_tables()
    P1.load_table('public','django_migrations')
    P1.get_table_schema('public','django_migrations')
    P1.close_cursor()
    P1.close_connection()

def display_table_selection():
    """
    --------------------
    Description
    --------------------
    -> display_table_selection (function): Function that displays the selection box for selecting the table to be analysed and triggers the loading of data (read_data())

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






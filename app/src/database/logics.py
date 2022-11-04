import sys
import psycopg2
from psycopg2 import OperationalError
import pandas as pd
import streamlit as st

from src.database.queries import get_tables_list_query, get_table_data_query, get_table_schema_query
class PostgresConnector:
    """
    --------------------
    Description
    --------------------
    -> PostgresConnector (class): Class that manages the connection to a Postgres database

    --------------------
    Attributes
    --------------------
    -> database (str): Name of Postgres database (mandatory)
    -> user (str): Username used for connecting to Postgres database (mandatory)
    -> password (str): Password used for connecting to Postgres database (mandatory)
    -> host (str): URL of Postgres database (mandatory)
    -> port (str): Port number of Postgres database (mandatory)
    -> conn (psycopg2._psycopg.connection): Postgres connection object (optional)
    -> cursor (psycopg2._psycopg.connection.cursor): Postgres cursor for executing query (optional)
    -> excluded_schemas (list): List containing the names of internal Postgres schemas to be excluded from selection (information_schema, pg_catalog)
    """

    def __init__(self, database="postgres", user='postgres', password='May@1990', port='5433',host='127.0.0.1'):
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.host = host
    def open_connection(self):
        """
        --------------------
        Description
        --------------------
        -> open_connection (method): Class method that creates an active connection to a Postgres database

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
        try:
            self.conn = psycopg2.connect(dbname=self.database, user=self.user, password=self.password, port=self.port, host=self.host)
            st.success('Connection to database Established!', icon="✅")
            with st.expander("Streamlite DataBase parameters"):
                st.write("{")
                st.write("menu text port :", self.port)
                st.write("database :", self.database)
                st.write("Menu password :",self.password)
                st.write("Menu User :", self.user)
                st.write("Connection : " , self.conn)
        except OperationalError as err:
            st.error(err)
            sys.exit(53)

    def close_connection(self):
        """
        --------------------
        Description
        --------------------
        -> close_connection (method): Class method that closes an active connection to a Postgres database

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
        try:
            self.conn.close()
            print('Connection to database Closed!')
        except OperationalError as err:
            st.error(err)
            sys.exit(53)

    def open_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> open_cursor (method): Class method that creates an active cursor to a Postgres database

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
        try:
            self.cursor = self.conn.cursor()
            print('Cursor opened')
        except OperationalError as err:
            st.error(err)
            sys.exit(53)
    def close_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> close_cursor (method): Class method that closes an active cursor to a Postgres database

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
        try:
            self.cursor.close()
        except OperationalError as err:
            st.error(err)
            sys.exit(53)

    def run_query(self, sql_query):
        """
        --------------------
        Description
        --------------------
        -> run_query (method): Class method that executes a SQL query and returns the result as a Pandas dataframe

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

    def list_tables(self):
        """
        --------------------
        Description
        --------------------
        -> list_tables (method): Class method that extracts the list of available tables using a SQL query (get_tables_list_query())

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
        try:
            """
            self.cursor.execute('select table_name from information_schema.tables')
            """
            self.cursor.execute(get_tables_list_query())
            table_records = self.cursor.fetchall()
            table_name_inp = st.selectbox('List of tables', options=table_records)
            st.text(table_name_inp)
            table = []
            for i in table_records:
                table.append(i[0])
            return (table)
        except OperationalError as err:
            st.error(err)
            sys.exit(53)



    def load_table(self, schema_name, table_name):
        """"
        --------------------
        Description
        --------------------
        -> load_table (method): Class method that load the content of a table using a SQL query (get_table_data_query())

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

        try:
            """
            load_table= pd.read_sql_query("select * from "+schema_name+"."+table_name+";", self.conn)
            """
            load_table = pd.read_sql_query(get_table_data_query('public','django_migrations'),self.conn)
            print(load_table)
            st.write(load_table)
        except OperationalError as err:
            st.error(err)
            sys.exit(53)

    def get_table_schema(self, schema_name, table_name):
        """
        --------------------
        Description
        --------------------
        -> get_table_schema (method): Class method that extracts the schema information of a table using a SQL query (get_table_schema_query())

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
        try:
            """
            get_table_schema = pd.read_sql_query("SELECT column_name, data_type FROM information_schema.columns "
                                                 "WHERE  table_name = '"+table_name+"' AND table_schema = '"+schema_name+"';",
                                                 self.conn)
            """
            get_table_schema = pd.read_sql_query(get_table_schema_query('public','django_migrations'), self.conn)
            print(get_table_schema)
            st.write(get_table_schema)
        except OperationalError as err:
            st.error(err)
            sys.exit(53)

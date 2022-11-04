import sys
def get_negative_number_query(schema_name='', table_name='', col_name=''):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has negative values
    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of the Database
    -> table_name (str): Name of the Table
    -> schema_name (str): Name of the Column
    --------------------
    Pseudo-Code
    --------------------
    ->Check if the length of the arguments is not zero or the arguments are not None
    ->Return the SQL query in string format by using SQL's COUNT function to determine how many rows a SELECT command returned
    --------------------
    Returns
    --------------------
    -> output (str): String for sql query

    """
    if len(schema_name)==0 and len(table_name)==0 and len(col_name)==0:
        print('No arguments')
        sys.exit(0)
    elif table_name==None and col_name==None:
        print('Empty table and column name string')
        sys.exit(1)
    elif table_name==None:
        print('Empty table name string')
        sys.exit(2)
    elif col_name==None:
        print('Empty column name string')
        sys.exit(3)
    return 'select count(*) from {} where {} <0'.format(table_name,col_name)
    

def get_std_query(schema_name='', table_name='', col_name=''):
    """
    --------------------
    Description
    --------------------
    -> get_std_query (method): Function that returns the query used for computing the standard deviation value of a column from a Postgres table
    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of the Database
    -> table_name (str): Name of the Table
    -> schema_name (str): Name of the Column
    --------------------
    Pseudo-Code
    --------------------
    ->Check if the length of the arguments is not zero or the arguments are not None
    ->Return the SQL query in string format by using SQL's STDDEV function that returns the population's standard deviation
    --------------------
    Returns
    --------------------
    -> output (str): String for sql query

    """
    if len(schema_name)==0 and len(table_name)==0 and len(col_name)==0:
        print('No arguments')
        sys.exit(0)
    elif table_name==None and col_name==None:
        print('Empty table and column name string')
        sys.exit(1)
    elif table_name==None:
        print('Empty table name string')
        sys.exit(2)
    elif col_name==None:
        print('Empty column name string')
        sys.exit(3)
    return 'select stddev({}) from {}'.format(col_name,table_name)


def get_unique_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_unique_query (method): Function that returns the query used for computing the number of unique values of a column from a Postgres table
    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of the Database
    -> table_name (str): Name of the Table
    -> schema_name (str): Name of the Column
    --------------------
    Pseudo-Code
    --------------------
    ->Check if the length of the arguments is not zero or the arguments are not None
    ->Use DISTINCT function is used to return distinct values in a column
    ->Use COUNT function on the top of DISTINCT function to to determine how many distinct rows a SELECT command returned
    ->Return the SQL query in string format
    --------------------
    Returns
    --------------------
    -> output (str): String for sql query
    """
    if len(schema_name)==0 and len(table_name)==0 and len(col_name)==0:
        print('No arguments')
        sys.exit(0)
    elif table_name==None and col_name==None:
        print('Empty table and column name string')
        sys.exit(1)
    elif table_name==None:
        print('Empty table name string')
        sys.exit(2)
    elif col_name==None:
        print('Empty column name string')
        sys.exit(3)
    return 'select count(distinct {}) from {}'.format(col_name,table_name)

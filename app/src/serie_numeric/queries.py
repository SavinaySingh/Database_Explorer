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
    if (schema_name==None and table_name==None and col_name==None) or (schema_name=='' and table_name=='' and col_name==''):
        print('No arguments')
        sys.exit(0)
    elif (schema_name==None and table_name==None) or (schema_name=='' and table_name==''):
        print('Empty schema and table name')
        sys.exit(1)
    elif (schema_name==None and col_name==None) or (schema_name=='' and col_name==''):
        print('Empty schema and column name')
        sys.exit(2)
    elif (table_name==None and col_name==None) or (table_name=='' and col_name==''):
        print('Empty table and column name')
        sys.exit(3)
    elif schema_name==None:
        print('Empty schema name')
        sys.exit(4)
    elif col_name==None:
        print('Empty column name')
        sys.exit(5)
    elif table_name==None:
        print('Empty table name')
        sys.exit(6)
    return 'select count(*) from {}.{} where {} <0'.format(schema_name,table_name,col_name)
    

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
    if (schema_name==None and table_name==None and col_name==None) or (schema_name=='' and table_name=='' and col_name==''):
        print('No arguments')
        sys.exit(7)
    elif (schema_name==None and table_name==None) or (schema_name=='' and table_name==''):
        print('Empty schema and table name')
        sys.exit(8)
    elif (schema_name==None and col_name==None) or (schema_name=='' and col_name==''):
        print('Empty schema and column name')
        sys.exit(9)
    elif (table_name==None and col_name==None) or (table_name=='' and col_name==''):
        print('Empty table and column name')
        sys.exit(10)
    elif schema_name==None:
        print('Empty schema name')
        sys.exit(11)
    elif col_name==None:
        print('Empty column name')
        sys.exit(12)
    elif table_name==None:
        print('Empty table name')
        sys.exit(13)
    return 'select stddev({}) from {}.{}'.format(col_name,schema_name,table_name)


def get_unique_query(schema_name='', table_name='', col_name=''):
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
    if (schema_name==None and table_name==None and col_name==None) or (schema_name=='' and table_name=='' and col_name==''):
        print('No arguments')
        sys.exit(14)
    elif (schema_name==None and table_name==None) or (schema_name=='' and table_name==''):
        print('Empty schema and table name')
        sys.exit(15)
    elif (schema_name==None and col_name==None) or (schema_name=='' and col_name==''):
        print('Empty schema and column name')
        sys.exit(16)
    elif (table_name==None and col_name==None) or (table_name=='' and col_name==''):
        print('Empty table and column name')
        sys.exit(17)
    elif schema_name==None:
        print('Empty schema name')
        sys.exit(18)
    elif col_name==None:
        print('Empty column name')
        sys.exit(19)
    elif table_name==None:
        print('Empty table name')
        sys.exit(20)
    return 'select count(distinct {}) from {}.{}'.format(col_name,schema_name,table_name)

def get_min_date_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_min_date_query (method): Function that returns the query used for computing the earliest date of a datetime column from a Postgres table

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
    ->Return the SQL query

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
    return """
        select min({col_name}) as EarliestDate
        from {table_name}
    """.format(col_name = col_name,table_name = table_name)
    
 

def get_weekend_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_weekend_count_query (method): Function that returns the query used for computing the number of times a date of a datetime column falls during weekends

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
    ->Return the SQL query

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
    return """ SELECT count({col_name})
                FROM {table_name} 
                WHERE EXTRACT(week FROM {col_name}) Not IN (0,5)
                """.format(col_name = col_name,table_name = table_name)
    
    

def get_1900_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_1900_count_query (method): Function that returns the query used for computing the number of times a datetime column has the value '1900-01-01'

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
    ->Return the SQL query

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
    return """
                select count({col_name})
                from {table_name} 
                where {col_name} = '1900-01-01'
    """.format(col_name = col_name,table_name = table_name)

     

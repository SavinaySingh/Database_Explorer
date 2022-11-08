def get_min_date_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_min_date_query (method): Function that returns the query used for computing the earliest date of a datetime column from a Postgres table

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
    query = """
        select min({col_name}) as EarliestDate
        from {table_name}
    """.format(col_name = col_name,table_name = table_name)

    return query

def get_weekend_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_weekend_count_query (method): Function that returns the query used for computing the number of times a date of a datetime column falls during weekends

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
    query = """ SELECT count({col_name})
                FROM {table_name} 
                WHERE EXTRACT(week FROM {col_name}) Not IN (0,5)
                """.format(col_name = col_name,table_name = table_name)
    
    return query

def get_1900_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_1900_count_query (method): Function that returns the query used for computing the number of times a datetime column has the value '1900-01-01'

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
    query = """
                select count({col_name})
                from {table_name} 
                where {col_name} = '1900-01-01'
    """.format(col_name = col_name,table_name = table_name)

    return query 

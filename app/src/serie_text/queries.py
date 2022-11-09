def get_missing_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_missing_query (method): Function that returns the query used for computing the number of missing values of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of the dataset schema
    -> table_name (str): Name of the dataset table 
    -> col_name (str): Name of the column 
    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    use select statement with count function to extract information table where column name us null.      

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """
    query = SELECT COUNT(*) FROM schema_name.table_name WHERE col_name= NULL;
    return query
 
def get_mode_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_mode_query (method): Function that returns the query used for computing the mode value of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> schema_name (str): Name of the dataset schema
    -> table_name (str): Name of the dataset table 
    -> col_name (str): Name of the column 
    --------------------

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
    query = SELECT
                col_name FROM
                (SELECT col_name,
                        cnt,
                        DENSE_RANK() OVER(ORDER BY cnt DESC
                        ) as rank
                    FROM
                        (SELECT col_name,
                                COUNT(*) as cnt
                            FROM
                                schema_name.table_name
                            GROUP By
                                col_name
                        ) x
                ) y
                WHERE
                rank = 1;
    return query

def get_alpha_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_alpha_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has only alphabetical characters

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> schema_name (str): Name of the dataset schema
    -> table_name (str): Name of the dataset table 
    -> col_name (str): Name of the column 
    --------------------

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
    return SELECT COUNT(col_name) FROM schema_name.table_name WHERE col_name NOT LIKE '%[^a-zA-Z ]%' AND col_name LIKE '%[a-zA-Z ]%';

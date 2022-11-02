def get_numeric_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_numeric_tables_query (method): Function that returns the query used for extracting the list of numeric columns from a Postgres table

    --------------------
    Parameters
    --------------------
    schema_name = the schema name for the particular table
    table_name = the name of the table whose numeric columns will be extracted

    --------------------
    Pseudo-Code
    --------------------
    
    query 
    return query

    --------------------
    Returns
    --------------------
    
    returns a query of type string

    """
    query = ("""select col.table_schema,col.table_name,col.ordinal_position as col_id,col.column_name,col.data_type,col.numeric_precision,col.numeric_scale
        from information_schema.columns col
        join information_schema.tables tab 
        on tab.table_schema = col.table_schema
        and tab.table_name = col.table_name
        and tab.table_type = 'BASE TABLE'
        where col.data_type in ('smallint', 'integer', 'bigint','decimal', 'numeric', 'real', 'double precision','smallserial', 'serial', 'bigserial', 'money')
        and col.table_schema not in ('information_schema', 'pg_catalog')
        and tab.table_name = '{0}'
        and tab.table_schema = '{1}'
        order by col.table_schema,
        col.table_name,
        col.ordinal_position;""".format(table_name,schema_name))
    
    return query

def get_text_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_text_tables_query (method): Function that returns the query used for extracting the list of text columns from a Postgres table

    --------------------
    Parameters
    --------------------
    schema_name = the schema name for the particular table
    table_name = the name of the table whose text columns will be extracted

    --------------------
    Pseudo-Code
    --------------------
    
    query 
    return query

    --------------------
    Returns
    --------------------
    
    returns a query of type string
    """
    query = ("""select col.table_schema,col.table_name,col.ordinal_position as column_id,col.column_name,col.data_type,col.character_maximum_length as maximum_length
        from information_schema.columns col
        join information_schema.tables tab 
        on tab.table_schema = col.table_schema
        and tab.table_name = col.table_name
        and tab.table_type = 'BASE TABLE'
        where col.data_type in ('character varying', 'character','text', '"char"', 'name')
        and col.table_schema not in ('information_schema', 'pg_catalog')
        and tab.table_name = '{0}'
        and tab.table_schema = '{1}'
        order by col.table_schema,
        col.table_name,
        col.ordinal_position;""".format(table_name,schema_name))
    
    return query

def get_date_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_date_tables_query (method): Function that returns the query used for extracting the list of datetime columns from a Postgres table

    --------------------
    Parameters
    --------------------
    schema_name = the schema name for the particular table
    table_name = the name of the table whose datetime columns will be extracted

    --------------------
    Pseudo-Code
    --------------------
    
    query 
    return query

    --------------------
    Returns
    --------------------
    
    returns a query of type string

    """
    query = ("""select col.table_schema,col.table_name,col.ordinal_position as column_id,col.column_name,col.data_type,col.character_maximum_length as maximum_length
        from information_schema.columns col
        join information_schema.tables tab 
        on tab.table_schema = col.table_schema
        and tab.table_name = col.table_name
        and tab.table_type = 'BASE TABLE'
        where col.data_type in ('timestamp without time zone','timestamp with time zone','time with time zone','time without time zone','interval', 'date')
        and col.table_schema not in ('information_schema', 'pg_catalog')
        and tab.table_name = '{0}'
        and tab.table_schema = '{1}'
        order by col.table_schema,
        col.table_name,
        col.ordinal_position;""".format(table_name,schema_name))
    
    return query

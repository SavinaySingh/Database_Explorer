def get_tables_list_query():
	"""
    --------------------
    Description
    --------------------
    -> get_tables_list_query (method): Function that returns the query used for extracting the list of tables from a Postgres table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    =>return("select table_name from information_schema.tables")
    -> pseudo-code

    --------------------
    Returns
    --------------------
    =>return("select * from "+schema_name+"."+table_name+";")


    """
	return("select table_name from information_schema.tables")
def get_table_data_query(schema_name, table_name):
	"""
    --------------------
    Description
    --------------------
    -> get_table_data_query (method): Function that returns the query used for extracting the content of a Postgres table

    --------------------
    Parameters
    --------------------
    => Schema name and table name
    --------------------
    Pseudo-Code
    --------------------
    =>return("select * from "+schema_name+"."+table_name+";")

   
    Returns
    --------------------
    => return("select * from "+schema_name+"."+table_name+";")


    """
	return("select * from "+schema_name+"."+table_name+";")


def get_table_schema_query(schema_name, table_name):
	"""
    --------------------
    Description
    --------------------
    -> get_table_schema_query (method): Function that returns the query used for extracting the list of columns from a Postgres table and their information

    --------------------
    Parameters
    --------------------
    =>  Schema name and table name

    --------------------
    Pseudo-Code
    --------------------
   	return("SELECT column_name, data_type FROM information_schema.columns WHERE  table_name = '"+table_name+"' AND table_schema = '"+schema_name+"';")


    --------------------
    Returns
    --------------------
   	return("SELECT column_name, data_type FROM information_schema.columns WHERE  table_name = '"+table_name+"' AND table_schema = '"+schema_name+"';")


    """
	return("SELECT column_name, data_type FROM information_schema.columns WHERE  table_name = '"+table_name+"' AND table_schema = '"+schema_name+"';")

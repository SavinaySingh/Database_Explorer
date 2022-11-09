import unittest
from queries import *

class Test_get_tables_list_query(unittest.TestCase):
    def test_get_tables_list_query(self):
        Expected = 'select table_name from information_schema.tables'
        Result = get_tables_list_query()
        self.assertEqual(Expected, Result)

class TestType_get_tables_list_query(unittest.TestCase):
    def test_get_tables_list_query(self):
        Expected = str
        Result = type(get_tables_list_query())
        self.assertEqual(Expected, Result)

class Test_get_table_data_query(unittest.TestCase):
    def test_get_table_data_query(self):
        Expected='select * from public.django_migrations;'
        Result=get_table_data_query('public', 'django_migrations')
        self.assertEqual(Expected, Result)

class TestType_get_table_data_query(unittest.TestCase):
    def test_get_table_data_query(self):
        Expected=str
        Result=type(get_table_data_query('public', 'django_migrations'))
        self.assertEqual(Expected, Result)

class Test_get_table_schema_query(unittest.TestCase):
    def test_get_table_data_query(self):
        Expected="SELECT column_name, data_type FROM information_schema.columns WHERE  table_name = 'django_migrations' AND table_schema = 'public';"
        Result=get_table_schema_query('public', 'django_migrations')
        self.assertEqual(Expected, Result)

class Type_Test_get_table_schema_query(unittest.TestCase):
    def test_get_table_data_query(self):
        Expected=str
        Result=type(get_table_schema_query('public', 'django_migrations'))
        self.assertEqual(Expected, Result)


if __name__ == '__main__':          
    unittest.main(verbosity=2)
 

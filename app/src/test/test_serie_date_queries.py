import unittest
import pandas as pd

from src.serie_date.queries import *

class TestGetMinDateQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='employees'
        col_name='birth_date'
        self.assertEqual(get_min_date_query(schema_name,table_name,col_name),'select count(*) from {} where {} <0'.format(table_name,col_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_min_date_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_min_date_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='birth_date'
        with self.assertRaises(SystemExit) as cm:
            get_min_date_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='employees'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_min_date_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)

class TestGetWeekEndCountQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='employees'
        col_name='birth_date'
        self.assertEqual(get_weekend_count_query(schema_name,table_name,col_name),'select count(*) from {} where {} <0'.format(table_name,col_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_weekend_count_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_weekend_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='birth_date'
        with self.assertRaises(SystemExit) as cm:
            get_weekend_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='employees'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_weekend_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)

class TestGet1900CountQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='employees'
        col_name='birth_date'
        self.assertEqual(get_1900_count_query(schema_name,table_name,col_name),'select count(*) from {} where {} <0'.format(table_name,col_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_1900_count_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_1900_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='birth_date'
        with self.assertRaises(SystemExit) as cm:
            get_1900_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='employees'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_1900_count_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

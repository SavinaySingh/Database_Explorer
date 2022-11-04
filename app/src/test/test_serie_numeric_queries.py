import unittest
import pandas as pd
import sys
sys.path.append(sys.path[0].replace('src/test',''))

from src.serie_numeric.queries import *

class TestGetNegativeNumberQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='order_details'
        col_name='product_id'
        self.assertEqual(get_negative_number_query(schema_name,table_name,col_name),'select count(*) from {} where {} <0'.format(table_name,col_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='product_id'
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='order_details'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)


class TestGetStandardDevQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='order_details'
        col_name='product_id'
        self.assertEqual(get_std_query(schema_name,table_name,col_name),'select stddev({}) from {}'.format(col_name,table_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_std_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='product_id'
        with self.assertRaises(SystemExit) as cm:
            get_std_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='order_details'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_std_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)

class TestUniqueQuery(unittest.TestCase):
    def test_correct_args(self):
        schema_name='postgres'
        table_name='order_details'
        col_name='product_id'
        self.assertEqual(get_unique_query(schema_name,table_name,col_name),'select count(distinct {}) from {}'.format(col_name,table_name), 'Wrong Output')
    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_negative_number_query()
        self.assertEqual(cm.exception.code, 0)
    def test_empty_table_column(self):
        schema_name='postgres'
        table_name=None
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_unique_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 1)
    def test_empty_table(self):
        schema_name='postgres'
        table_name=None
        col_name='product_id'
        with self.assertRaises(SystemExit) as cm:
            get_unique_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 2)
    def test_empty_column(self):
        schema_name='postgres'
        table_name='order_details'
        col_name=None
        with self.assertRaises(SystemExit) as cm:
            get_unique_query(schema_name,table_name,col_name)
        self.assertEqual(cm.exception.code, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)

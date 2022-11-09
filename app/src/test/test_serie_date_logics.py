import unittest
import pandas as pd
import numpy as np
import sys
import pandas.io.sql as sqlio
sys.path.append(sys.path[0].replace('src/test',''))
from serie_date.logics import DateColumn
from serie_date.queries import get_1900_count_query,get_min_date_query,get_weekend_count_query

class TestDateColumnInstantiation(unittest.TestCase):
    date_var=DateColumn()
    def test_serie(self):
        self.assertEqual(self.date_var.serie,None,'Not None')
    def test_n_unique(self):
        self.assertEqual(self.date_var.n_unique,None,'Not None')
    def test_n_missing(self):
        self.assertEqual(self.date_var.n_missing,None,'Not None')
    def test_col_min(self):
        self.assertEqual(self.date_var.col_min,None,'Not None')
    def test_col_max(self):
        self.assertEqual(self.date_var.col_max,None,'Not None')
    def test_n_weekend(self):
        self.assertEqual(self.date_var.n_weekend,None,'Not None')
    def test_n_weekday(self):
        self.assertEqual(self.date_var.n_weekday,None,'Not None')
    def test_n_future(self):
        self.assertEqual(self.date_var.n_future,None,'Not None')
    def test_n_empty_1900(self):
        self.assertEqual(self.date_var.n_empty_1900,None,'Not None')
    def test_n_empty_1970(self):
        self.assertEqual(self.date_var.n_empty_1970,None,'Not None')
    def test_n_barchart(self):
        self.assertEqual(self.date_var.n_barchart,None,'Not None')
    def test_n_frequent(self):
        self.assertEqual(self.date_var.frequent,None,'Not None')
    

class TestSetData(unittest.TestCase):
    date_var=DateColumn(ttable_name='employees',col_name='birth_date')
    def test_self_data(self):
        date_var1=DateColumn(table_name='employees',col_name='birth_date')
        date_var1.set_data()
        test_serie=sqlio.read_sql_query('select {} from {}'.format('discount','order_details'), date_var1.db.conn)[date_var1.col_name]
        for i in range(0,len(date_var1.serie)):
            self.assertEqual(date_var1.serie[i],test_serie[i],'Incorrect')

class TestIsSerieNone(unittest.TestCase):
    date_var=DateColumn(table_name='employees',col_name='birth_date')
    def test_serie(self):
        date_var1=DateColumn(table_name='employees',col_name='birth_date')
        date_var1.set_data()
        self.assertEqual(date_var1.is_serie_none(),False,'Incorrect')

class TestSetUnique(unittest.TestCase):
    date_var = DateColumn(table_name='employees',col_name='birth_date')
    def test_serie(self):
        date_var1 = DateColumn(table_name='employees',col_name='birth_date')
        date_var1.set_unique()
        self.assertEqual(date_var1.n_unique,10,'Incorrect')

class TestSetMissing(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_missing(self):
        date_var1=DateColumn(table_name='order_details',col_name='discount')
        date_var1.set_data()
        date_var1.set_missing()
        self.assertEqual(date_var1.n_missing,len(date_var1.serie[date_var1.serie==np.nan]),'Incorrect')

class TestSetMin(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_col_min(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_min()
        sql=get_min_date_query(date_var.db.database,date_var.table_name,date_var.col_name)
        self.assertEqual(date_var.col_min,sqlio.read_sql_query(sql,date_var.db.conn),'Incorrect')

class TestSetMax(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_col_max(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_max()
        self.assertEqual(date_var.col_max,date_var.serie.max(),'Incorrect')

class TestSetWeekend(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_weekend(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_weekend()
        sql=get_weekend_count_query(date_var.db.database,date_var.table_name,date_var.col_name)
        self.assertEqual(date_var.n_weekend,sqlio.read_sql_query(sql,date_var.db.conn),'Incorrect')

class TestSetWeekday(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_weekday(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_weekday()
        self.assertEqual(date_var.n_weekday,date_var.serie.dt.dayofweek,'Incorrect')
    
class TestSetFuture(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_future(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_future()
        self.assertEqual(date_var.n_future,len(self.serie(pd.to_datetime("today").strftime("%m/%d/%Y"))),'Incorrect')

class TestSetEmpty1900(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_empty_1900(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_empty_1900()
        sql=get_1900_count_query(date_var.db.database,date_var.table_name,date_var.col_name)
        self.assertEqual(date_var.n_empty_1900,sqlio.read_sql_query(sql,date_var.db.conn),'Incorrect')

class TestSetEmtpy1970(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_n_empty_1970(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_empty_1970()
        self.assertEqual(date_var.n_empty_1970,len(self.serie.isin(['1970-01-01'])),'Incorrect')

class TestSetBarchart(unittest.TestCase):
    date_var=DateColumn(table_name='order_details',col_name='discount')
    def test_barchart(self):
        date_var=DateColumn(table_name='order_details',col_name='discount')
        date_var.set_data()
        date_var.set_barchart()
        self.assertEqual(str(type(date_var.n_barchart)),"<class 'altair.vegalite.v4.api.Chart'>",'Incorrect')


if __name__ == '__main__':
    unittest.main(verbosity=2)

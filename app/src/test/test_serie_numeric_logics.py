import unittest
import pandas as pd
import sys
import altair as alt
import pandas.io.sql as sqlio
import numpy as np
#print(sys.path[0].replace('src/test',''))
sys.path.append(sys.path[0].replace('src/test',''))

from src.serie_numeric.logics import NumericColumn
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class TestNumericColumnInstantiation(unittest.TestCase):
    numeric=NumericColumn()
    def test_serie(self):
        self.assertEqual(self.numeric.serie,None,'Not None')
    def test_n_unique(self):
        self.assertEqual(self.numeric.n_unique,None,'Not None')
    def test_n_missing(self):
        self.assertEqual(self.numeric.n_missing,None,'Not None')
    def test_col_mean(self):
        self.assertEqual(self.numeric.col_mean,None,'Not None')
    def test_col_std(self):
        self.assertEqual(self.numeric.col_std,None,'Not None')
    def test_col_min(self):
        self.assertEqual(self.numeric.col_min,None,'Not None')
    def test_col_max(self):
        self.assertEqual(self.numeric.col_max,None,'Not None')
    def test_col_median(self):
        self.assertEqual(self.numeric.col_median,None,'Not None')
    def test_col_n_zeros(self):
        self.assertEqual(self.numeric.n_zeros,None,'Not None')
    def test_col_n_negatives(self):
        self.assertEqual(self.numeric.n_negatives,None,'Not None')
    def test_col_histogram(self):
        self.assertEqual(self.numeric.histogram,None,'Not None')
    def test_col_frequent(self):
        self.assertEqual(self.numeric.frequent,None,'Not None')
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_table_name(self):
        self.assertEqual(self.numeric.table_name,'order_details','Incorrect table name')
    def test_col_name(self):
        self.assertEqual(self.numeric.col_name,'discount','Incorrect column name')
    def test_schema_name(self):
        self.assertEqual(self.numeric.db.database,'postgres','Incorrect schema name')

class TestSetData(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_self_data_without_init(self):
        self.assertEqual(self.numeric.serie,None,'Incorrect')
    def test_self_data_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        test_serie=sqlio.read_sql_query('select {} from {}'.format('discount','order_details'), numeric2.db.conn)[numeric2.col_name]
        for i in range(0,len(numeric2.serie)):
            self.assertEqual(numeric2.serie[i],test_serie[i],'Incorrect')
        numeric2.db.close_connection()
class TestIsSerieNone(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_serie_before_init(self):
        self.assertEqual(self.numeric.is_serie_none(),True,'Incorrect')
    def test_serie_after_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        self.assertEqual(numeric2.is_serie_none(),False,'Incorrect')
        numeric2.db.close_connection()

class TestSetUnique(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_n_unique_without_init(self):
        self.assertEqual(self.numeric.n_unique,None,'Incorrect')
    def test_n_unique_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_unique()
        self.assertEqual(numeric2.n_unique,11,'Incorrect')
        numeric2.db.close_connection()

class TestSetMissing(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_n_missing_without_init(self):
        self.assertEqual(self.numeric.n_missing,None,'Incorrect')
    def test_n_missing_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_missing()
        self.assertEqual(numeric2.n_missing,len(numeric2.serie[numeric2.serie==np.nan]),'Incorrect')
        numeric2.db.close_connection()

class TestSetZeros(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_n_zeros_without_init(self):
        self.assertEqual(self.numeric.n_zeros,None,'Incorrect')
    def test_n_zeros_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_zeros()
        self.assertEqual(numeric2.n_zeros,len(numeric2.serie[numeric2.serie==0]),'Incorrect')
        numeric2.db.close_connection()

class TestSetNegatives(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_n_zeros_without_init(self):
        self.assertEqual(self.numeric.n_negatives,None,'Incorrect')
    def test_n_zeros_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_negatives()
        sql=get_negative_number_query(numeric2.schema_name,numeric2.table_name,numeric2.col_name)
        self.assertEqual(numeric2.n_negatives,sqlio.read_sql_query(sql,numeric2.db.conn)['count'][0],'Incorrect')
        numeric2.db.close_connection()

class TestSetMean(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_col_mean_without_init(self):
        self.assertEqual(self.numeric.col_mean,None,'Incorrect')
    def test_col_mean_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_mean()
        self.assertEqual(numeric2.col_mean,numeric2.serie.mean(),'Incorrect')
        numeric2.db.close_connection()
class TestSetStd(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_col_std_without_init(self):
        self.assertEqual(self.numeric.col_std,None,'Incorrect')
    def test_col_std_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_std()
        sql=get_std_query(numeric2.schema_name,numeric2.table_name,numeric2.col_name)
        self.assertEqual(numeric2.col_std,sqlio.read_sql_query(sql,numeric2.db.conn)['stddev'][0],'Incorrect')
        numeric2.db.close_connection()
class TestSetMin(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_col_min_without_init(self):
        self.assertEqual(self.numeric.col_min,None,'Incorrect')
    def test_col_min_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_min()
        self.assertEqual(numeric2.col_min,numeric2.serie.min(),'Incorrect')
        numeric2.db.close_connection()

class TestSetMax(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_col_max_without_init(self):
        self.assertEqual(self.numeric.col_max,None,'Incorrect')
    def test_col_max_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_max()
        self.assertEqual(numeric2.col_max,numeric2.serie.max(),'Incorrect')
        numeric2.db.close_connection()

class TestSetMedian(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_col_median_without_init(self):
        self.assertEqual(self.numeric.col_median,None,'Incorrect')
    def test_col_median_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_median()
        self.assertEqual(numeric2.col_median,numeric2.serie.median(),'Incorrect')
        numeric2.db.close_connection()

class TestSetHistogram(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_histogram_without_init(self):
        self.assertEqual(self.numeric.histogram,None,'Incorrect')
    def test_histogram_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_histogram()
        self.assertEqual(str(type(numeric2.histogram)),"<class 'altair.vegalite.v4.api.Chart'>",'Incorrect')
        numeric2.db.close_connection()

class TestSetFrequent(unittest.TestCase):
    numeric=NumericColumn(table_name='order_details',col_name='discount')
    def test_frequent_without_init(self):
        self.assertEqual(self.numeric.frequent,None,'Incorrect')
    def test_frequent_with_init(self):
        numeric2=NumericColumn(table_name='order_details',col_name='discount')
        numeric2.db.open_connection()
        numeric2.set_data()
        numeric2.set_frequent()
        df_test=pd.DataFrame([numeric2.serie.value_counts().index[0]],columns=['Most Frequent Value'])
        for i in range(0,len(df_test)):
            self.assertEqual(numeric2.frequent['Most Frequent Value'][i],df_test['Most Frequent Value'][i],'Incorrect')
        numeric2.db.close_connection()

class TestGetSummaryDataframe(unittest.TestCase):

    def test_get_summary(self):
        numeric=NumericColumn(table_name='order_details',col_name='discount')
        ans=numeric.get_summary_df()
        dict_test={('Number of unique value of a serie',numeric.n_unique),
                        ('Number of missing values of a serie',numeric.n_missing),
                        ('Average value of a serie',numeric.col_mean),
                        ('Standard deviation value of a serie',numeric.col_std),
                        ('Minimum value of a serie',numeric.col_min),
                        ('Maximum value of a serie',numeric.col_max),
                        ('Median value of a serie',numeric.col_median),
                        ('Number of times a serie has values equal to 0',numeric.n_zeros),
                        ('Number of times a serie has negative values',numeric.n_negatives)}
        self.assertEqual(ans,dict_test,'Incorrect')


if __name__ == '__main__':
    unittest.main(verbosity=2)

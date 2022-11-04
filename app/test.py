#import streamlit as st
#
#from src.serie_numeric.logics import NumericColumn
#
#
#d=NumericColumn()
#d.set_data()
#d.set_unique()
#d.set_missing()
#d.set_zeros()
#d.set_negatives()
#d.set_mean()
#d.set_std()
#d.set_min()
#d.set_max()
#d.set_median()
#d.set_frequent()
#d.get_summary_df()
from src.serie_numeric.display import display_numerics
display_numerics()

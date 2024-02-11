import streamlit as st
import pandas as pd
import numpy as np

# df = pd.DataFrame(
#     # np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

df = pd.read_csv('data.csv')

st.map(df, use_container_width=True)
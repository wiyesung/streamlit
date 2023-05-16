import streamlit as st
import munpy as np
import pandas as pd

st.title("MAP")
df = pd.DataFrame(np.random.randn(500,2) / [50, 50] + {37.76, -122.4],columns=['lat','lon'])
st.map(df)
# x = st.slider('Selext a value')
# st.write(x, 'squared is', x * x)

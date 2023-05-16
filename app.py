import streamlit as st

x = st.slider('Selext a value')
st.write(x, 'squared is', x * x)

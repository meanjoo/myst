import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)

st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])

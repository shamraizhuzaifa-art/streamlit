import numpy as np
import streamlit as st

arr = [100,200,300,400,500]

st.write("Mean:", np.mean(arr))
st.write("Max:", np.max(arr))
st.write("Min:", np.min(arr))

# visualization
st.line_chart(arr)

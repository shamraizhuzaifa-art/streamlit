import pandas as pd
import numpy as np
import streamlit as st

arr = [100,200,300,400,500]

st.write("Mean:", np.mean(arr))
st.write("Max:", np.max(arr))
st.write("Min:", np.min(arr))

# visualization
st.line_chart(arr)
st.bar_chart(arr)
st.area_chart(arr)
st.map(pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']))
file = st.file_uploader("Upload a CSV file", type="csv")

if file is not None:
    df = pd.read_csv(file)
    st.write(df)

# a = input("Enter a number: ")
# print("You entered:", a)
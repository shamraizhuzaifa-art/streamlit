import numpy as np
import pandas as pd 
import streamlit as st
file =st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    df = df.dropna()
    st.write(df)

import pandas as pd;
import streamlit as st;

st.title("working with pandas and streamit.")

uploaded_file = st.file_uploader("please upload your file here.")

if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df.describe())
else:
  st.write("file not uploaded")
  
df.write(df.head())
  

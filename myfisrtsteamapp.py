import streamlit as st
import pandas as pd
st.write("""
#My first app

Hello *world!* Srinivas!!
""")
df = pd.read_csv("oracle_test_data.csv")
st.write(df)

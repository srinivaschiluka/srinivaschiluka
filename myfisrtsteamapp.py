import streamlit as st
import pandas as pd
st.write("""
#My first app

Hello *world!* Srinivas!!
""")
df = pd.read_csv("mycsv.csv")
st.line_chart(df)

import streamlit as st
import pandas as pd

url = "http://localhost:8000/namespaces"

df = pd.read_json(url)

with st.container():
    st.button(label="Refresh", on_click=st.write(df))

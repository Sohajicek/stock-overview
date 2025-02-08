import streamlit as st
from utils import process_product_data

uploaded_files = st.file_uploader(
    label="Choose a CSV file", type=["xlsx"], accept_multiple_files=True
)
st.session_state.data = process_product_data(uploaded_files)
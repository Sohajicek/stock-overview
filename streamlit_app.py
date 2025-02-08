import streamlit as st


if "product" not in st.session_state:
    st.session_state.product = None
if "data" not in st.session_state:
    st.session_state.data = None
if "files" not in st.session_state:
    st.session_state.files = []

upload_page = st.Page("pages/upload_page.py", title="Nahrání souborů")
summary_page = st.Page("pages/summary_page.py", title="Přehled")
product_page = st.Page("pages/product_page.py", title="Produkt")

pg = st.navigation([upload_page, summary_page, product_page])
pg.run()
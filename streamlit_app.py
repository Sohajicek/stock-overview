import streamlit as st


if "product" not in st.session_state:
    st.session_state.product = None
if "data" not in st.session_state:
    st.session_state.data = None
if "pages" not in st.session_state:
    st.session_state.pages = {}
if "files" not in st.session_state:
    st.session_state.files = []

upload_page = st.Page("pages/upload_page.py", title="Nahrání souborů")
summary_page = st.Page("pages/summary_page.py", title="Přehled")
product_page = st.Page("pages/product_page.py", title="Produkt")

st.session_state.pages["upload"] = upload_page
st.session_state.pages["summary"] = summary_page
st.session_state.pages["product"] = product_page

pg = st.navigation([upload_page, summary_page, product_page])
pg.run()
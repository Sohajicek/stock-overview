import streamlit as st
from utils import plot_product_data

st.header(f"Produkt {st.session_state.product}")

if st.session_state.data is None:
  st.write("Nebyly nalezeny záznamy")
else:
  # st.write(st.session_state.data[st.session_state.product])
  plot_product_data(st.session_state.data[st.session_state.product])

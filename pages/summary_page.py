import streamlit as st
import re

st.header("Souhrn")

if st.session_state.data is None:
  st.write("Nebyly nalezeny záznamy")
else:
  products = []
  for product, data in st.session_state.data.items():
    if len(data["Prodej"]) > 1:
      def split_product(product):
        match = re.match(r"(.*)-(\d+)-(\d+)$", product)
        if match:
          return match.groups()
        else:
          return None

      product_name, material, factory = split_product(product)
      ammount = data["Prodej"][-1][1]

      products.append({"Produkt": product_name, "Materiál": material, "Závod": factory, "Zakoupených kusů": ammount}) 

  products.sort(key=lambda x: x["Zakoupených kusů"], reverse=True)

  event = st.dataframe(products, use_container_width=True, selection_mode="single-row", on_select="rerun")
  
  if len(event.selection.rows) > 0:
    product = products[event.selection.rows[0]]
    st.session_state.product = f"{product["Produkt"]}-{product['Materiál']}-{product['Závod']}"
    st.switch_page("pages/product_page.py")

st.write("Pro detail produktu zaškrtněte řádek v levém políčku.")

st.header("Nahrané soubory:")
for file in st.session_state.files:
  st.write(f"**{file.name}**")
import streamlit as st

st.header("Souhrn")

if st.session_state.data is None:
  st.write("Nebyly nalezeny záznamy")
else:
  sorted_products = {}
  for product, data in st.session_state.data.items():
    # st.write(f"{product}")
    # st.write(data["Prodej"])
    # break
    # st.write(data)
    if len(data["Prodej"]) > 1:
      sorted_products[product] = data["Prodej"][-1][1]
  
  sorted_products = dict(sorted(sorted_products.items(), key=lambda x: x[1], reverse=True))
  
  # st.write(sorted_products)
  # config = {
  #     "1": "Produkt",
  #     "2": "Zakoupených kusů",
  # }
  config = {
      "product": st.column_config.TextColumn("Produkt", max_chars=100, width="medium"),
      "sold": st.column_config.NumberColumn("Zakoupených kusů", width="small"),
  }
  event = st.dataframe(sorted_products, use_container_width=True, selection_mode="single-row", on_select="rerun", column_config=config)
  
  if len(event.selection.rows) > 0:
    st.session_state.product = list(sorted_products.keys())[event.selection.rows[0]]
    st.switch_page("pages/product_page.py")
  
  
  # if st.button("Zkopírovat seřazený souhrn", key=f"copy-summary"):
    
  
  # for product, value in sorted_products.items():
  #   col1, col2 = st.columns([0.7, 0.3], vertical_alignment="center")
  #   col1.write(product)
  #   # if col1.button(product, key=product, help="Zobrazit detail produktu"):
  #   #   st.session_state.product = product
  #   if col2.button(str(value), key=f"{product}-1"):
  #     st.session_state.product = product
    
    # label = f"{value} -- {product}"
    # if st.button(label, key=product, help="Zobrazit detail produktu"):
    #   st.session_state.product = product
  
  # stable_products = []
  # dynamic_products = []

  # for product, data in st.session_state.data.items():
  #   dynamic = False
  #   for val in data.values():
  #       if not len(set([v[1] for v in val])) == 1:
  #         dynamic = True
  #         break
  #   if dynamic:
  #     dynamic_products.append(product)
  #   else:
  #     stable_products.append(product)
  
  # id = 0
  # option_dynamic = st.selectbox(
  #   "Produkty s měnícím se stavem zásob",
  #   (dynamic_products),
  #   index=None,
  #   placeholder="Výběr hodnoty"
  # )
  # option_stable = st.selectbox(
  #   "Produkty se stálým stavem zásob",
  #   (stable_products),
  #   index=None,
  #   placeholder="Výběr hodnoty"
  # )
  
  # if option_dynamic is not None or option_stable is not None:
  #   st.session_state.product = option_dynamic if option_dynamic else option_stable
  #   st.switch_page("pages/product_page.py")
    

st.header("Nahrané soubory:")
for file in st.session_state.files:
  st.write(f"**{file.name}**")
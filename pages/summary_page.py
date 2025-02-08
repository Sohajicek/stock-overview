import streamlit as st

st.header("Souhrn")

if st.session_state.data is None:
  st.write("Nebyly nalezeny záznamy")
else:
  stable_products = []
  dynamic_products = []

  for product, data in st.session_state.data.items():
    for val in data.values():
        if not len(set([v[1] for v in val])) == 1:
            dynamic_products.append(product)
            break
    stable_products.append(product)
  
  id = 0
  option_dynamic = st.selectbox(
    "Produkty s měnícím se stavem zásob",
    (dynamic_products),
    index=None,
    placeholder="Výběr hodnoty"
  )
  option_stable = st.selectbox(
    "Produkty se stálým stavem zásob",
    (stable_products),
    index=None,
    placeholder="Výběr hodnoty"
  )
  
  if option_dynamic is not None or option_stable is not None:
    st.session_state.product = option_dynamic if option_dynamic else option_stable
    st.switch_page(st.session_state.pages["product"])
    
  
  
  # st.write("Produkty s měnícím se stavem zásob")
  # for product in dynamic_products:
  #   id += 1
  #   if st.button(product, key=id):
  #     st.session_state.product = product

  # st.write("Produkty se stálým stavem zásob")
  # for product in stable_products:
  #   id += 1
  #   if st.button(product, key=id):
  #     st.session_state.product = product
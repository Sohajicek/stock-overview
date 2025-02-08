import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def process_product_data(files):
    # Dictionary to store data for each product
    product_data = defaultdict(lambda: defaultdict(list))

    filenames = []
    for file in files:
        st.write(file.name)
        date = file.name.split('/')[-1].split(' ')[1].replace('.', ',')
        day, month, year = date.split(',')
        filenames.append({'name': file, 'day': day, 'month': month, 'year': year})
        
    # st.write(sorted_filenames)
    sorted_filenames = sorted(filenames, key=lambda f: (int(f['year']), int(f['month']), int(f['day'])))  
    # st.write(sorted_filenames)

    for file in sorted_filenames:        
        df = pd.read_excel(file['name'], header=None)[5:-1]
        
        # Sort the dataframe by the second and third columns
        df_sorted = df.sort_values([df.columns[1], df.columns[2]], ascending=[True, True])
        
        for _, row in df_sorted.iterrows():
            product_name = row[0]
            material = row[1]
            factory = row[2]
            product_key = f"{product_name}-{material}-{factory}"
            date_key = f"{file['day']}/{file['month']}/{file['year']}"
            
            column_names = ["Součet z Skladem", "Součet z Volně použitelná", "Součet z Příjde na sklad", "Součet z Otevřené zakázky"]
            for col_name, value in zip(column_names, row[[3, 4, 5, 7]]):
                product_data[product_key][col_name].append((date_key, value))

    for p_key, p_value in product_data.items():
        # st.write(p_key)
        # st.write(p_value)
        day, prev_val = p_value["Součet z Skladem"][0]
        prev_sale = 0
        p_value["Prodej"].append((day, prev_sale))
        if len(p_value["Součet z Skladem"]) > 1:            
            for day, value in p_value["Součet z Skladem"][1:]:
                # st.write({day: value})
                if value < prev_val:
                    prev_sale = prev_sale + prev_val - value
                p_value["Prodej"].append((day, prev_sale))
                prev_val = value
        
        # st.write(p_value["Prodej"])
        # break
                
    return product_data

def plot_product_data(product, data):
    dates = [date for date, _ in data[list(data.keys())[0]]]
    df = pd.DataFrame({column: [value for _, value in values] for column, values in data.items()}, index=dates)
    st.line_chart(df)
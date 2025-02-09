import streamlit as st
import pandas as pd
from collections import defaultdict


def process_product_data(files):
    product_data = defaultdict(lambda: defaultdict(list))

    filenames = []
    for file in files:
        st.write(file.name)
        date = file.name.split('/')[-1].split(' ')[1].replace('.', ',')
        day, month, year = date.split(',')
        filenames.append({'name': file, 'day': day, 'month': month, 'year': year})

    sorted_filenames = sorted(filenames, key=lambda f: (int(f['year']), int(f['month']), int(f['day'])))

    for file in sorted_filenames:        
        df = pd.read_excel(file['name'], header=None)[5:-1]
        df_sorted = df.sort_values([df.columns[1], df.columns[2]], ascending=[True, True])
        
        for _, row in df_sorted.iterrows():
            product_name = row[0]
            material = row[1]
            factory = row[2]
            product_key = f"{product_name}-{material}-{factory}"
            date_key = f"{file['day']}/{file['month']}/{file['year']}"
            
            column_names = ["Skladem", "Volně použitelná", "Příjde na sklad", "Otevřené zakázky"]
            for col_name, value in zip(column_names, row[[3, 4, 5, 7]]):
                product_data[product_key][col_name].append((date_key, value))

    for _, p_value in product_data.items():
        day, prev_val = p_value["Skladem"][0]
        prev_sale = 0
        p_value["Prodej"].append((day, prev_sale))
        if len(p_value["Skladem"]) > 1:            
            for day, value in p_value["Skladem"][1:]:
                if value < prev_val:
                    prev_sale = prev_sale + prev_val - value
                p_value["Prodej"].append((day, prev_sale))
                prev_val = value
                                
    return product_data

def plot_product_data(data):
    dates = [date for date, _ in data[list(data.keys())[0]]]
    df = pd.DataFrame({column: [value for _, value in values] for column, values in data.items()}, index=dates)
    st.line_chart(df)
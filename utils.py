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
            
            column_names = ["Součet z Skladem", "Součet z Volně použitelná", "Součet z Příjde na sklad", "Součet z Neuvolněno", "Součet z Otevřené zakázky", "Součet z Blokováno", "Součet z V kontrole jakosti", "Součet z Pojistná zásoba", "Součet z Objednávky SK 4500xxx"]
            for col_name, value in zip(column_names, row[3:]):
                product_data[f"{product_name}-{material}-{factory}"][col_name].append((f"{file['day']}/{file['month']}/{file['year']}", value))
    
    return product_data

def plot_product_data(product, data):    
    # fig = plt.figure(figsize=(10, 3))
    fig = plt.figure()
    for column, values in data.items():
        # print(column, values)
        dates, y_values = zip(*values)
        plt.plot(dates, y_values, label=column)
    plt.title(f"{product}")
    plt.xlabel("Datum")
    plt.ylabel("Počet")
    plt.legend(bbox_to_anchor=(0.5,0), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
import streamlit as st
import pandas as pd
import numpy as np

# df = pd.DataFrame(
#     # np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

import streamlit as st
import requests
import hashlib
import time
import pandas as pd
import random

def string_to_color(text):
    # Check if color already assigned to the string
    if text in colors_dict:
        return colors_dict[text]
    else:
        while True:
            # Generate random color values between 0 and 255
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            # Check if the generated color is unique
            if color not in colors_dict.values():
                colors_dict[text] = color
                return color

# Function to fetch CSV file from server
def fetch_csv_file(url):
    response = requests.get(url)
    return response.text


# Define URL of the CSV file on the server
CSV_URL = "https://acab-193-232-210-148.ngrok-free.app/"
cnt = 0
title = st.title('Метки проб')
old_pd = pd.read_csv('data.csv')

colors_dict = {}
# text = st.text('hello')
# df_st = st.write(pd.read_csv('data.csv'),use_container_width=True)
# old_pd['color'] = old_pd['text'].apply(lambda x: string_to_color(x))
text = st.text('Карта с информацией о полученных пробах; Разные цвета - разные категории')

# map = st.map(old_pd)


csv_data = fetch_csv_file(CSV_URL)
        # text.text(f'{csv_data}')

with open("map.csv",'w') as f:
    f.write(csv_data)


df = pd.read_csv("map.csv")
df['color'] = df['specie_name'].apply(lambda x: string_to_color(x))
# df_st.write(df)
# st.write(df)


map = st.map(df,color='color',size = 10, use_container_width=True)
while True:
    try:    
        # Fetch CSV file from server
        csv_data = fetch_csv_file(CSV_URL)
        # text.text(f'{csv_data}')

        with open("map.csv",'w') as f:
            f.write(csv_data)

        
        df = pd.read_csv("map.csv")
        df['color'] = df['specie_name'].apply(lambda x: string_to_color(x))
        # df_st.write(df)
        # st.write(df)


        map.map(df,color='color',size=10, use_container_width=True)
        # st.title(f"Count: {cnt}")

    except Exception as e:
        st.error(f"Error: {e}")

    # Wait for some time before checking again
    time.sleep(3)  # Check every minute


# df = pd.read_csv('data.csv')

# st.map(df, use_container_width=True)


# import streamlit as st
# import time

# # Function to fetch new data from the server
# def fetch_data_from_server(x):
#     # Simulating fetching data from server
#     new_data = {"x": [1,2,3], "y": [x*1,x*2,x*3]}  # Example data
#     return new_data

# def main():
#     title = st.title("Dynamic Data Visualization Example")
    
#     # Create an empty plot to update dynamically
#     chart = st.line_chart()
#     cnt = 0
#     # Update the chart with new data from the server every second
#     while True:
#         new_data = fetch_data_from_server(cnt)
#         cnt+=1
#         title.title(f'Title: {cnt}')
#         chart.line_chart(new_data)
#         time.sleep(5)

# if __name__ == "__main__":
#     main()


import streamlit

streamlit.title('\N{peach} \N{cherries} My Healthy Diner \N{coconut} \N{banana}')

streamlit.header('Breakfast Menu')
streamlit.text('\N{red apple} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# set index
my_fruit_list = my_fruit_list.set_index('Fruit')

# a pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table 
streamlit.dataframe(fruits_to_show);

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

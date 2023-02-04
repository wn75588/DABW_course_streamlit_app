
import streamlit

streamlit.title('\N{peach} \N{cherries} My Healthy Diner \N{coconut} \N{banana}')

streamlit.header('Breakfast Menu')
streamlit.text('\N{red apple} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

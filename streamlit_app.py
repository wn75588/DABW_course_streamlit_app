
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('\N{peach} \N{cherries} My Healthy Diner \N{coconut} \N{banana}')

streamlit.header('Breakfast Menu')
streamlit.text('\N{red apple} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# set index
my_fruit_list = my_fruit_list.set_index('Fruit')

# a pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table 
streamlit.dataframe(fruits_to_show);


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
   else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
    streamlit.error()
    
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")

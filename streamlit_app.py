import streamlit
import pandas
import snowflake.connector

streamlit.title(' My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
fruit_choice = streamlit.text_input("fruit?: ", 'apple')

fruityvice_result = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
streamlit.text(fruityvice_result.json())

fruit_c = streamlit.text_input("fruit?: ", "loquat")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

def get_fruit_load():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button("gimme the fruit"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text("data:")
  streamlit.dataframe(get_fruit_load)
  


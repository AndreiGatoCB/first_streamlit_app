import streamlit
import pandas as pd

streamlit.title('My parents new healthy dinner.')

streamlit.header('Breakfast menu.')
streamlit.text(' 🥣  Omega 3 & Blueberry Oatmeal.')
streamlit.text(' 🥗  Kale, spinach & rocker smoothie.')
streamlit.text(' 🐔  Hard-boiled free-range egg.')
streamlit.text(' 🥑🍞  Avocado toast.')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

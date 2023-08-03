import streamlit

streamlit.title("My Google Form Sheet Responses")
  
streamlit.header('Responses')
streamlit.text('We take responses from our customers to reflect on it & provide a quality expertice dining to them')

import pandas
my_response_list = pandas.read_csv("https://docs.google.com/spreadsheets/d/1QtWmX5YQD5aswwOYOYerlwdWNwZcmFkxWTr_zAbV9Rk/edit?usp=sharing")
streamlit.dataframe(my_response_list)

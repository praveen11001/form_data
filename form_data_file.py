import streamlit

streamlit.title("My Google Form Sheet Responses")
  
streamlit.header('Responses')
streamlit.text('We take responses from our customers to reflect on it & provide a quality expertice dining to them')

import pandas
my_response_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_response_list)

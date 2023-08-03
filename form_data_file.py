import streamlit as st
import pandas as pd

st.title("My Google Form Sheet Responses")
st.header('Responses')
st.text('We take responses from our customers to reflect on it & provide a quality expertise dining to them')

# Read the data from the URL into a DataFrame
url = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_response_list = pd.read_csv(url)


st.dataframe(my_response_list)

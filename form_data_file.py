import streamlit as st
import pandas as pd

st.title("My Google Form Sheet Responses")
st.header('Responses')
st.text('We take responses from our customers to reflect on it & provide a quality expertise dining to them')

# Read the data from the URL into a DataFrame
url = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_response_list = pd.read_csv(url)

# Function to apply color coding to calories column
def highlight_calories(s):
    is_max = s == s.max()
    is_min = s == s.min()
    return ['background-color: red' if v else 'background-color: green' for v in is_max]

# Apply the highlight function to the DataFrame and display it
st.dataframe(my_response_list.style.apply(highlight_calories, subset=['calories'], axis=0))

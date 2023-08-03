import streamlit as st
import pandas as pd

st.title("My Google Form Sheet Responses")
st.header('Responses')
st.text('We take responses from our customers to reflect on it & provide a quality expertise dining to them')

# Read the data from the URL into a DataFrame
url = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_response_list = pd.read_csv(url)




# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 27],
    'Score': [85, 92, 78, 80]
}

df = pd.DataFrame(my_response_list)

# Function to apply color to the "Age" column based on a condition
def color_age(val):
    color = 'red' if val < 25 else 'black'
    return f'color: {color}'

# Apply the style to the DataFrame
styled_df = df.style.applymap(color_age, subset=['Calories'])

# Display the styled DataFrame
styled_df

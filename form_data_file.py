import streamlit as st
import pandas as pd

st.title("My Google Form Sheet Responses")
st.header('Responses')
st.text('We take responses from our customers to reflect on it & provide a quality expertise dining to them')

# Read the data from the URL into a DataFrame
url = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_response_list = pd.read_csv(url)


df = pd.DataFrame(my_response_list)

# Function to apply color to the "Age" column based on a condition
def color_age(val):
    color = ''

    if val < 25:
        color = 'red'
    elif val > 25 and val < 50:
        color = 'yellow'
    else:
        color = 'green'
        
    return f'color: {color}'

# Apply the style to the DataFrame
styled_df = df.style.applymap(color_age, subset=['Calories'])

# Display the styled DataFrame
styled_df

import streamlit as st
import pandas as pd

st.title("My Google Form Sheet Responses")
st.header('Responses')
st.text('We take responses from our customers to reflect on it & provide a quality expertise dining to them')

# Read the data from the URL into a DataFrame
url = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_response_list = pd.read_csv(url)


df = pd.DataFrame(my_response_list)

# ---------------
csv_link = 'https://docs.google.com/spreadsheets/d/1QtWmX5YQD5aswwOYOYerlwdWNwZcmFkxWTr_zAbV9Rk/edit?usp=sharing'

# Read the CSV data into a pandas DataFrame
new_data = pd.read_csv(csv_link)

# Now you can work with the 'df' DataFrame containing your Google Sheets data
pd.dataframe(new_data)
# ---------------

# Function to apply color to the "Age" column based on a condition
def color_age(val):
    color = ''

    if val >= 25 and val <= 60:
        color = 'green'
    elif val > 60 and val <= 90:
        color = 'yellow'
    else:
        color = 'red'
        
    return f'color: {color}'

# Apply the style to the DataFrame
styled_df = df.style.applymap(color_age, subset=['Calories'])

# Display the styled DataFrame
styled_df

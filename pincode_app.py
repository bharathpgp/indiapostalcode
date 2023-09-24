import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

# Streamlit app title
st.title("India Postal/PIN Code Lookup")

# Input for PIN code
pincode = st.text_input("Enter PIN code:", key='pincode', help="<input autofocus>")

# Define the API URL
api_url = f"https://api.data.gov.in/resource/5c2f62fe-5afa-4119-a499-fec9d604d5bd?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&filters%5Bpincode%5D={pincode}"

# Function to make the API request and parse the response
def fetch_pincode_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("records", [])
    else:
        return None

# Display results or error message
if pincode:
    pincode_data = fetch_pincode_data(api_url)
    if pincode_data:
        st.subheader("PIN Code Details:")
        # Create a DataFrame from the records
        df = pd.DataFrame(pincode_data)
        st.table(df)
    else:
        st.error("No records found for the entered PIN code. Please check the PIN code.")

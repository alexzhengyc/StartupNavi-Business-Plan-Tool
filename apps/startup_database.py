import streamlit as st
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("your_mongoDB_connection_string")
db = client['your_database']


st.title("Startup Database")

# Input for startup search
search_term = st.text_input("Search Startups by Keyword:")

if search_term:
    # Search MongoDB for startups matching the keyword
    results = db.startup_collection.find({"$text": {"$search": search_term}})
    startup_data = list(results)

    # Convert results to a DataFrame
    import pandas as pd
    df = pd.DataFrame(startup_data)

    # Display DataFrame
    st.dataframe(df)

import streamlit as st
import pandas as pd
import os

# File path for storing chat history
HISTORY_FILE = "chat_history.csv"

# Load research data from CSV
@st.cache_data
def load_research_data():
    return pd.read_csv('research_data.csv')

# Search function
def search_research(query, df):
    query = query.lower()
    filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    return filtered_df

# Load chat history from file
def load_chat_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    else:
        return pd.DataFrame(columns=["Query", "Title", "Keywords", "Year", "Student", "Supervisor"])

# Save chat history to file
def save_chat_history(chat_history):
    chat_history.to_csv(HISTORY_FILE, index=False)

# Set page config
st.set_page_config(page_title="Research Chatbot", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: darkblue;'>Department of Information Technology, FMSC, USJ</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📚 Research Chatbot</h2>", unsafe_allow_

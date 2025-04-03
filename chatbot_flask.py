import streamlit as st
import pandas as pd
import os

# Function to generate a unique session ID for each user
def get_session_id():
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(id(st.session_state))
    return st.session_state.session_id

# Load research data from CSV
@st.cache_data
def load_research_data():
    return pd.read_csv('research_data.csv')

# Search function
def search_research(query, df):
    query = query.lower()
    filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    return filtered_df

# Load chat history from file for a specific session
def load_chat_history(session_id):
    session_history_file = f"chat_history_{session_id}.csv"
    if os.path.exists(session_history_file):
        return pd.read_csv(session_history_file)
    else:
        return pd.DataFrame(columns=["Query", "Title", "Keywords", "Year", "Student", "Supervisor"])

# Save chat history to file for a specific session
def save_chat_history(chat_history, session_id):
    session_history_file = f"chat_history_{session_id}.csv"
    chat_history.to_csv(session_history_file, index=False)

# Set page config
st.set_page_config(page_title="Research Chatbot", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: darkblue;'>Department of Information Technology, FMSC, USJ</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📚

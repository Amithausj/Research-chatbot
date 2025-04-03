import streamlit as st
import pandas as pd

# Load research data from CSV
@st.cache_data
def load_research_data():
    df = pd.read_csv('research_data.csv')
    return df

# Search function
def search_research(query, df):
    query = query.lower()
    filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    return filtered_df

# Set page config
st.set_page_config(page_title="Research Chatbot", layout="wide")

# Header
st.markdown(
    "<h1 style='text-align: center; color: darkblue;'>Department of Information Technology, FMSC, USJ</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='text-align: center;'>📚 Research Chatbot</h2>",
    unsafe_allow_html=True,
)

# Load data
df = load_research_data()

# Session State to Store Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = pd.DataFrame(columns=["Query", "Title", "Keywords", "Year", "Student", "Supervisor"])

# --- UI Layout ---
# Search box & button at the top
st.markdown("### 🔍 Ask about research topics:")
user_query = st.text_input("Enter your question:")

if st.button("Search"):
    if user_query:
        results = search_research(user_query, df)
        if results.empty:
            st.error("❌ No matching research found.")
        else:
            # Add user query and results to chat history
            results.insert(0, "Query", user_query)  # Add query as first column
            st.session_state_

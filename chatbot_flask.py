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
    st.session_state.chat_history = []

# --- UI Layout ---
# Search box & button at the top
st.markdown("### 🔍 Ask about research topics:")
user_query = st.text_input("Enter your question:")

if st.button("Search"):
    if user_query:
        results = search_research(user_query, df)
        if results.empty:
            response_text = "❌ No matching research found."
            results_df = pd.DataFrame(columns=["Title", "Keywords", "Year", "Student", "Supervisor"])
        else:
            response_text = "✅ Search Results:"
            results_df = results  # Display the filtered results in a table format

        # Save to chat history
        st.session_state.chat_history.append((user_query, results_df))
    else:
        st.warning("⚠️ Please enter a query.")

# --- Display Search Results (Table) ---
st.markdown("---")
st.markdown("### 📊 Search Results")
if st.session_state.chat_history:
    last_query, last_results = st.session_state.chat_history[-1]
    st.write(f"**You: {last_query}**")
    if last_results.empty:
        st.error("❌ No matching research found.")
    else:
        st.dataframe(last_results)  # Display results in a table format

# Footer
st.markdown(
    "<hr><p style='text-align: center;'>© 2025 : Department of Information Technology, FMSC, USJ</p>",
    unsafe_allow_html=True,
)

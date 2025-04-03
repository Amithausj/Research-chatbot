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
        else:
            response_text = f"✅ Search Results:\n\n{results.to_string(index=False)}"

        # Save to chat history
        st.session_state.chat_history.append(("You: " + user_query, "Chatbot: " + response_text))
    else:
        st.warning("⚠️ Please enter a query.")

# --- Display Chat History ---
st.markdown("---")
st.markdown("### 🗨️ Chat History")
for user, bot in reversed(st.session_state.chat_history):  # Show latest messages first
    st.write(f"**{user}**")
    st.info(bot)

# Footer
st.markdown(
    "<hr><p style='text-align: center;'>© 2025 : Department of Information Technology, FMSC, USJ</p>",
    unsafe_allow_html=True,
)

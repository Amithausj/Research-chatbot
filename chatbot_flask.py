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

# Streamlit UI
st.title("Department of Information Technology, FMSC, USJ")
st.title("📚 Research Chatbot")
#st.body("© 2025 : Department of Information Technology, FMSC, USJ")

# Load the data
df = load_research_data()

# User input
user_query = st.text_input("Ask about research topics:")

if st.button("Search"):
    if user_query:
        results = search_research(user_query, df)
        if results.empty:
            st.write("❌ No matching research found.")
        else:
            st.write("✅ Search Results:")
            st.dataframe(results)
    else:
        st.write("⚠️ Please enter a query.")


import pandas as pd

# Step 1: Load the research data from the CSV file
def load_research_data():
    # Load the CSV file into a pandas DataFrame
    return pd.read_csv('research_data.csv')

# Step 2: Define the function to search all columns
def get_research_info(query, data):
    # Convert the query to lowercase to ensure case-insensitive matching
    query = query.lower()

    # Step 2.1: Search across all columns in the DataFrame
    # We check if the query appears in any column (case-insensitive)
    results = data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)

    # Step 2.2: Filter results and return them
    filtered_data = data[results]

    if not filtered_data.empty:
        return filtered_data.to_string(index=False)  # Return the found data as string (formatted)
    else:
        return "Sorry, no research found for your query."

# Step 3: Define the chatbot logic
def chatbot():
    print("Hello! I am your research assistant chatbot. Type 'quit' to exit.")

    # Load research data into the bot
    data = load_research_data()

    while True:
        # Ask user for input
        query = input("You: ").lower()

        if query == 'quit':
            print("Chatbot: Goodbye!")
            break

        # Search for research topics matching the query
        response = get_research_info(query, data)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()

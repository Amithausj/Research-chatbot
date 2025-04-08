import pandas as pd
from flask import Flask, render_template, request, jsonify

# Step 1: Load the research data from the CSV file
def load_research_data():
    # Load the CSV file into a pandas DataFrame
    return pd.read_csv('research_data.csv')

# Step 2: Define the function to search all columns
def get_research_info(query, data):
    # Convert the query to lowercase to ensure case-insensitive matching
    query = query.lower()

    # Search across all columns in the DataFrame
    results = data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)

    # Filter results
    filtered_data = data[results]

    if not filtered_data.empty:
        # Generate HTML table rows from the filtered data
        table_rows = ""
        for _, row in filtered_data.iterrows():
            table_rows += f"""
                <tr>
                    <td>{row['Title']}</td>
                    <td>{row['Keywords']}</td>
                    <td>{row['Year']}</td>
                    <td>{row['Student']}</td>
                    <td>{row['Supervisor']}</td>
                     <td>{row['Type']}</td>
                </tr>
            """
        return table_rows
    else:
        return "Sorry, no research found for your query."


# Step 3: Set up Flask
app = Flask(__name__)

@app.route('/')
def home():
    # Display the chatbot page
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    # Get the user query from the request
    user_query = request.form['query'].lower()

    # Load the research data
    data = load_research_data()

    # Get the chatbot's response based on the query
    response = get_research_info(user_query, data)

    # Return the response as a JSON object to be displayed on the webpage
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)

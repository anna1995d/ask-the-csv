import os
import pandas as pd
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

# Set the page configuration
st.title("📉 Ask the CSV")

# Set the file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
st.write("Upload a CSV file and explore it with the help of GPT.")

if uploaded_file:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    # Display dataset summary
    st.subheader("Dataset Summary")
    rows, cols = df.shape
    st.write(f"Rows: {rows} | Columns: {cols}")
    st.write("Columns:", list(df.columns))

    # Load environment variables
    # Ensure you have a .env file with your OpenAI API key
    # Example: OPENAI_API_KEY=your_api_key
    load_dotenv()
    # Initialize OpenAI client
    client = OpenAI()

    # Create summary prompt
    summary = "The dataset has the following columns:\n"
    for col in df.columns:
        # Print column details
        summary += f"- {col} ({df[col].dtype})\n"

    # Add a few rows of the dataset to the summary
    summary += "\nHere are the first 5 rows of the dataset:\n"
    summary += df.head().to_string(index=False)

    # Display the summary
    st.code(summary)

    # Create a text input for the user to ask questions
    question = st.text_input("Ask a question about the dataset:")

    prompt = f"""You are an expert data analyst. Here is a summary of the dataset:
            {summary}

            User question: {question}

            Answer the question as clearly as possible."""
    

    if question:
        try:
            with st.spinner("Thinking..."):
                # Call OpenAI API
                response = client.chat.completions.create(
                    model = "gpt-3.5-turbo",
                    messages = [
                        {"role": "system", "content": "You are a helpful data analyst. Keep answers concise."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature = 0.3,
                )

                # Display the answer
                answer = response.choices[0].message.content
                
                st.subheader("Answer:")
                st.write(answer)

                if "qa_history" in st.session_state:
                    st.session_state.qa_history.append((question, answer))

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown("---")
with st.expander("Chat History", expanded=False):
    if st.session_state.qa_history:
        st.subheader("Chat History")
        # Add a button to clear chat history
        if st.button("Clear Chat History"):
            st.session_state.qa_history.clear()

        for i, (q, a) in enumerate(st.session_state.qa_history, 1):
            st.markdown(f"**Q{i}:** {q}")
            st.markdown(f"**A{i}:** {a}")
            st.markdown("---")



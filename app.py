import openai
import streamlit as st

# Access the API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate text with continuous stream
def generate_text(prompt):
    # Initialize an empty string for the response
    response_text = ""

    # Create a placeholder to update the message progressively
    chat_placeholder = st.empty()

    # Stream the response from the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a well-read journalist aware of India's recent performance in the 2024 Paralympics."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,  # Adjust token length as needed
        stream=True
    )

    # Update the response in chunks to simulate streaming
    for chunk in response:
        # Extract and append the latest part of the response
        response_text += chunk['choices'][0]['delta'].get('content', '')
        chat_placeholder.write(response_text)

    # Return final response text
    return response_text

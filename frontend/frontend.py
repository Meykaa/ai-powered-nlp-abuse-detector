import streamlit as st
import requests
import json

# URL of the Flask backend
BACKEND_URL = "http://127.0.0.1:5000/analyze"

# Streamlit UI
st.title("AI-Powered Social Media Comment Analyzer")

st.write(
    "Enter a comment below, and we'll analyze it for any harmful content like abuse, body shaming, racism, and more."
)

# Textbox for user to enter the comment with reduced height
comment = st.text_area("Comment:", "", height=80)  # Reduced height to 80

# Submit button
if st.button("Analyze Comment"):
    if comment.strip() == "":
        st.warning("Please enter a comment to analyze.")
    else:
        # Sending the comment to the Flask backend for analysis
        try:
            response = requests.post(
                BACKEND_URL, json={"comment": comment}
            )

            if response.status_code == 200:
                result = response.json()
                category = result.get("category", "Unknown")
                note = result.get("note", "No additional notes provided.")

                # Display the results
                st.subheader("Analysis Result:")
                st.write(f"**Category**: {category}")
                st.write(f"**Note**: {note}")

            else:
                st.error(f"Error: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"API request error: {e}")

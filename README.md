# AI-Powered Social Media Comment Analyzer

1.1 Problem Statement:

Social media platforms are often flooded with harmful comments including abuse, hate speech, racism, and body shaming. Manually moderating such content is time-consuming, inconsistent, and prone to bias. There is a pressing need for an automated system to assist in detecting and flagging such abusive content in real-time.

1.2 Solution:

This project is an **AI-Powered Social Media Comment Analyzer** that uses Natural Language Processing (NLP) to analyze user-submitted comments and classify them into categories like:

- Abusive
- Hate Speech
- Body Shaming
- Racism
- or Non-Harmful

Additionally, the tool provides personalized feedback or constructive guidance, encouraging users to engage in healthier online conversations and promoting respectful behavior.

# Features

- Automatically detects harmful comments in real-time
- Classifies comments into predefined categories
- Generates personalized, constructive feedback based on the comment's tone
- Utilizes pre-trained Sentence Transformers for accurate semantic understanding
- Interactive, user-friendly interface built with Streamlit
- Flask backend API for seamless real-time analysis

# Tech Stack

- Frontend: Streamlit
- Backend : Flask (REST API)
- ML Model: Sentence Transformers (`all-MiniLM-L6-v2`)
- Language: Python

# How to Run Locally

1. Clone the repository

- git clone https://github.com/yourusername/ai-comment-analyzer.git
- cd ai-comment-analyzer

2. Create a virtual environment
- python -m venv venv
- source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies
- pip install -r requirements.txt

4. Run the Flask backend
- cd backend
- python app.py
 
5. Run the Streamlit frontend
- Open a new terminal:
- cd frontend
- streamlit run app.py

# Demo Screenshot

1. Abusive Comment Example
   [Abusive Result](assets/sample1_page-0001.jpg)

2. Insensitive Comment Example 
   [Insensitive result](assets/sample2_page-0001.jpg)

3. Respectful comment Example
   [Respectful Result](assets/sample3_page-0001.jpg)

# Future Improvements

- Integrate with social media APIs for live moderation
- Add multi-language support
- Include severity score for moderation thresholds
- Deploy to cloud for public access


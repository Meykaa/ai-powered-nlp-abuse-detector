from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load the Mistral API key from the .env file
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise ValueError("❌ MISTRAL_API_KEY not found! Please check your .env file.")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Social Media Abuse Detector API!"})

@app.route("/analyze", methods=["POST"])
def analyze_comment():
    data = request.get_json()
    if not data or "comment" not in data:
        return jsonify({"error": "No comment provided"}), 400

    comment = data["comment"]
    result = generate_comment_analysis_with_mistral(comment)
    
    return jsonify(result), 200

def generate_comment_analysis_with_mistral(comment):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are an AI content moderation assistant. "
        "Your job is to analyze user comments and classify them into one of the following categories:\n\n"
        "- respectful\n"
        "- hurtful\n"
        "- abusive\n"
        "- body shaming\n"
        "- racist\n"
        "- sexist\n"
        "- threatening\n"
        "- insensitive (mental health, disability, trauma, etc.)\n"
        "- constructive criticism\n"
        "- other\n\n"
        "Then, write a short, kind, and non-repetitive educational note (if needed) to discourage harmful behavior "
        "and promote respectful online communication. If the comment is respectful or constructive, just mention that politely."
    )

    user_prompt = (
        f"Comment: \"{comment}\"\n\n"
        "Return a JSON object like this:\n"
        "{\n"
        "  \"category\": \"racist\",\n"
        "  \"note\": \"Racism is never acceptable. Let's create an inclusive environment for all.\""
        "} "
    )

    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "{}")

        # Safely evaluate content to ensure it returns a valid JSON response
        result = eval(content) if content.startswith("{") else {"category": "unknown", "note": "⚠️ Could not analyze comment."}
        return result

    except Exception as e:
        return {
            "category": "error",
            "note": f"API error: {str(e)}"
        }

if __name__ == "__main__":
    app.run(debug=True)

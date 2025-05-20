from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
CORS(app)
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/message", methods=["POST"])
def message():
    data = request.get_json().get("message")
    print(data)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[data],
        config=types.GenerateContentConfig(
            max_output_tokens=250,
        ),
    )
    return jsonify(response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

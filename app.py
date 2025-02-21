from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv
import os

load_dotenv()
hugging_face_token = os.getenv("HUGGING_FACE_TOKEN")

from huggingface_hub import login
login(token = hugging_face_token)


# Initialize the Flask application
app = Flask(__name__)

# Load the Qwen2.5-32B-Instruct model and tokenizer from Hugging Face
model_name = "openai-community/gpt2"  # Specify the model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define a root route
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def query():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.json
        user_message = json_data.get('message', None)

        if user_message:
            # Tokenize input and generate response
            inputs = tokenizer(user_message, return_tensors='pt')
            outputs = model.generate(**inputs, max_length=150)
            response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return jsonify({"response": response_text})
        else:
            return jsonify({"error": "No message was found"}), 400
    else:
        return jsonify({"error": "Content-Type not supported!"}), 415

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
CORS(app)  # Allow frontend access

# Load the model
model = OllamaLLM(model="llama3")
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

conversation_history = []  # Store conversation history

@app.route("/")
def home():
    return render_template("index.html")  # Serve the frontend

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Limit conversation history to 5 messages
    if len(conversation_history) > 5:
        conversation_history.pop(0)

    context = "\n".join(conversation_history)
    result = chain.invoke({"context": context, "question": user_input})

    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"AI: {result}")

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)

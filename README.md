# AI Chatbot with Flask, LangChain, and Ollama

This is a simple AI chatbot using **Flask** for the backend, **LangChain** with **Ollama** for AI responses, and a **modern dark-themed frontend**.

## 🚀 Features
- **Full-screen Chat UI** with a black background and white text.
- **LangChain + Ollama** integration for AI responses.
- **Flask API** for message handling.
- **Auto-scroll** and **Enter key support**.
- **Frontend with HTML, CSS, and JavaScript**.

---

## 📌 Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **Virtual Environment** (recommended)
- **Node.js** (if you want to extend the frontend later)

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/ananyaudupa/chat_bot.git
 cd chatbot-project
```

### 2️⃣ Create a Virtual Environment
```sh
 python -m venv env
```

### 3️⃣ Activate Virtual Environment  
#### **Windows:**
```sh
 env\Scripts\activate
```
#### **Mac/Linux:**
```sh
 source env/bin/activate
```

### 4️⃣ Install Dependencies
```sh
 pip install -r requirements.txt
```
_(If `flask_cors` is missing, install it separately:)_  
```sh
 pip install flask-cors
```

### 5️⃣ Run the Flask Server
```sh
 python main.py
```

After running, the server will start on:
```
 http://127.0.0.1:5000/
```

---

## 🖥️ Frontend Structure

- **`templates/index.html`** → Main chat UI.
- **`static/style.css`** → Dark theme styling.
- **`static/script.js`** → Handles user input & API calls.

---

## 🚀 How to Use
1. Open your browser and go to: **http://127.0.0.1:5000/**
2. Type a message in the input box.
3. Press **Enter** or click **Send**.
4. The AI will respond instantly!

---

## 📂 Project Structure
```
chatbot-project/
│── env/                # Virtual environment (ignored in Git)
│── templates/
│   └── index.html      # Chat UI
│── static/
│   ├── style.css       # Stylesheet for dark theme
│   ├── script.js       # Handles chat interactions
│── main.py             # Flask backend (API + AI logic)
│── requirements.txt    # Python dependencies
│── README.md           # This file
```

---

## 🔧 API Endpoint
**POST /chat**  
Sends a user message to the AI and gets a response.

**Example Request:**
```sh
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello!"}'
```

**Response:**
```json
{
  "response": "Hello! How can I help you?"
}
```

---

## 💡 Future Improvements
- 🔊 **Voice Input Support**
- 🤖 **Persistent Conversation History**
- 🌍 **Deployment on Render or Heroku**

---

## 🛠️ Troubleshooting
❌ `ModuleNotFoundError: No module named 'flask_cors'`
- Run: `pip install flask-cors`

❌ `Could not locate a Flask application`
- Ensure `main.py` has `app = Flask(__name__)` and is being run properly.

---

## 📜 License
This project is **open-source**. Feel free to modify and improve it! 🚀

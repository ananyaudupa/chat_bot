function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;  // Prevent empty messages

    let chatBox = document.getElementById("chat-box");

    // Display user message
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = ""; // Clear input

    // Scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send message to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
    })
    .catch(error => console.error("Error:", error));
}

// Allow sending message by pressing Enter key
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

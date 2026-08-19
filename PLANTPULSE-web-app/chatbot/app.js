async function generateAnswer(userinput) {
    try {
        // TODO: Add your Gemini API key below
        const GEMINI_API_KEY = "YOUR_GEMINI_API_KEY";
        const responsedata = await axios({
            url: `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${GEMINI_API_KEY}`,
            method: "post",
            data: {
                contents: [
                    {
                        parts: [{ text: `${userinput}` }],
                    },
                ],
            },
        });

        // Extract the chatbot's response
        let data = responsedata.data.candidates[0].content.parts[0].text;
        data = data.replace(/\*\*/g, '');

        return data;
    } catch (error) {
        console.error("Error fetching response:", error);
        return "Sorry, I couldn't understand that. Please try again.";
    }
}

async function sendMessage() {
    const userInput = document.getElementById("userInput").value.trim();

    if (!userInput) {
        alert("Please type a message!");
        return;
    }

    // Display the user's message in the chat
    displayMessage(userInput, "You");

    // Clear the input field
    document.getElementById("userInput").value = "";

    // Generate the chatbot's response
    const botResponse = await generateAnswer(userInput);

    // Display the chatbot's response in the chat
    displayMessage(botResponse, "AI");
}

function displayMessage(message, sender) {
    const chatMessages = document.querySelector('.chat-messages');

    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    if (sender === 'You') {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('bot-message');
    }

    const senderLabel = document.createElement('strong');
    senderLabel.textContent = `${sender}: `;
    messageElement.appendChild(senderLabel);

    const messageText = document.createElement('span');
    messageText.textContent = message;
    messageElement.appendChild(messageText);

    chatMessages.appendChild(messageElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="The All New Orin Speed AI", layout="wide")
st.title("Orin Speed")
st.write("Puter Name = AIfree")
st.write("Puter Password = artificialIT!1")
html_code = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(130deg, #8A2BE2, #1E90FF, #00FFFF, #8A2BE2);
            background-size: 400% 400%;
            animation: neonMove 16s ease infinite;
            font-family: Arial, sans-serif;
            color: #fff;
            display: flex;
            justify-content: center;
        }
        @keyframes neonMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        #chat-container {
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            background: rgba(0,0,0,0.35);
            backdrop-filter: blur(12px);
        }
        #chat {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: transparent;
        }
        .message {
            margin: 10px 0;
            padding: 12px 20px;
            border-radius: 18px;
            max-width: 80%;
            line-height: 1.5;
            word-wrap: break-word;
            font-size: 16px;
            box-shadow: 0 0 8px rgba(0,255,255,0.6);
        }
        .user {
            background: rgba(255,0,255,0.3);
            color: #fff;
            align-self: flex-end;
            border-bottom-right-radius: 0;
            box-shadow: 0 0 12px #ff00ff;
        }
        .ai {
            background: rgba(0,255,255,0.3);
            color: #0ff;
            align-self: flex-start;
            border-bottom-left-radius: 0;
            font-size: 18px;
            white-space: pre-wrap;
            box-shadow: 0 0 12px #0ff;
        }
        #input-container {
            display: flex;
            padding: 15px;
            background: rgba(0,0,0,0.35);
            border-top: 1px solid #0ff;
        }
        #user_input {
            flex: 1;
            border-radius: 25px;
            padding: 14px 20px;
            border: 1px solid #0ff;
            background: rgba(0,0,0,0.6);
            color: #fff;
            outline: none;
            font-size: 16px;
        }
        #send-btn {
            margin-left: 10px;
            padding: 14px 24px;
            border-radius: 25px;
            border: none;
            background: #1E90FF;
            color: white;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 0 10px #1E90FF;
        }
        #send-btn:hover {
            background: #00FFFF;
            box-shadow: 0 0 12px #00FFFF;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #0ff;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #1E90FF;
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <div id="chat"></div>
        <div id="input-container">
            <input type="text" id="user_input" placeholder="Type your message..." />
            <button id="send-btn">Send</button>
        </div>
    </div>
    <script src="https://js.puter.com/v2/"></script>
    <script>
        const chatDiv = document.getElementById("chat");
        const userInput = document.getElementById("user_input");
        const sendBtn = document.getElementById("send-btn");
        function appendMessage(text, sender) {
            const msg = document.createElement("div");
            msg.className = "message " + sender;
            msg.innerText = text;
            chatDiv.appendChild(msg);
            chatDiv.scrollTop = chatDiv.scrollHeight;
        }
        function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;
            appendMessage(message, "user");
            userInput.value = "";
            puter.ai.chat(message, { model: "gpt-5.2-chat" })
                .then(response => {
                    let content = "";
                    if (response.message && response.message.content) {
                        if (typeof response.message.content === "string") {
                            content = response.message.content;
                        } else if (Array.isArray(response.message.content)) {
                            content = response.message.content.map(c => c.text || "").join("\\n");
                        } else {
                            content = JSON.stringify(response.message.content);
                        }
                    } else {
                        content = "No response from AI";
                    }
                    appendMessage("Orin Speed: " + content, "ai");
                })
                .catch(err => {
                    appendMessage("Orin Speed: Sorry, There was an error. If you are a developer, you an use this error message to help You! error - " + JSON.stringify(err), "ai");
                });
        }
        sendBtn.addEventListener("click", sendMessage);
        userInput.addEventListener("keypress", function(e) {
            if (e.key === "Enter") {
                e.preventDefault();
                sendMessage();
            }
        });
    </script>
</body>
</html>"""
st.markdown("""
<style>
/* Full neon gradient for the entire Streamlit app */
body, [data-testid="stAppViewContainer"] > .main, .css-18e3th9 {
    height: 100vh;
    background: linear-gradient(130deg, #8A2BE2, #1E90FF, #00FFFF, #8A2BE2);
    background-size: 400% 400%;
    animation: neonMove 16s ease infinite;
    overflow: hidden;
}

/* Neon animation keyframes */
@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Optional: hide Streamlit footer and header for fullscreen look */
footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

components.html(html_code, height=900, scrolling=True)
st.write("Published 28th January 2026")
st.write("Copywright Orin Intelligence©")

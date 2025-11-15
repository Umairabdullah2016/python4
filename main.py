import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="UAserver AI Chat", layout="wide")
st.title(" UAserver AI 2.5")
st.write("Name = AIfree")
st.write("code = artificialIT!1")

# Fullscreen chat HTML/JS
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: #0d1117;
            font-family: Arial, sans-serif;
            color: #fff;
            display: flex;
            justify-content: center;
        }

        #chat-container {
            width: 100%;
            max-width: 1000px;
            height: 100vh;
            display: flex;
            flex-direction: column;
            background: #161b22;
        }

        #chat {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }

        .message {
            margin: 10px 0;
            padding: 12px 20px;
            border-radius: 18px;
            max-width: 75%;
            line-height: 1.5;
            word-wrap: break-word;
            font-size: 16px;
        }

        .user {
            background: #238636;
            color: #fff;
            align-self: flex-end;
            border-bottom-right-radius: 0;
        }

        .ai {
            background: #1e2732;
            color: cyan;
            align-self: flex-start;
            border-bottom-left-radius: 0;
            font-size: 18px;
            white-space: pre-wrap;
        }

        #input-container {
            display: flex;
            padding: 15px;
            border-top: 1px solid #30363d;
            background: #161b22;
        }

        #user_input {
            flex: 1;
            border-radius: 25px;
            padding: 14px 20px;
            border: 1px solid #30363d;
            background: #0d1117;
            color: #fff;
            outline: none;
            font-size: 16px;
        }

        #send-btn {
            margin-left: 10px;
            padding: 14px 24px;
            border-radius: 25px;
            border: none;
            background: #238636;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }

        #send-btn:hover {
            background: #2ea043;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #30363d;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #484f58;
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

            // Call Puter AI
            puter.ai.chat(message, { model: "gemini-2.5-flash" })
            
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

                    appendMessage("🔷 UAserver AI: " + content, "ai");
                })

                .catch(err => {
                    appendMessage("🔷 UAserver AI: Error - " + JSON.stringify(err), "ai");
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
</html>
"""


components.html(html_code, height=900, scrolling=True)

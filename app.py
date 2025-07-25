# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:26:47 2025

@author: zhi yan
"""

from flask import Flask, request, render_template_string, jsonify
from chatbot import JewelChangiFAQ
import random

app = Flask(__name__)

BOT_GREETINGS = [
    "✈️ Ready for your Jewel Changi adventure? Ask me anything!",
    "🎉 Welcome to Jewel! What would you like to know today?",
    "✨ Your airport experience starts here! How can I help?"
]

faq = JewelChangiFAQ()

@app.route('/', methods=['GET', 'POST'])
def home():
    random_greeting = random.choice(BOT_GREETINGS)
    return render_template_string(HTML_TEMPLATE, random_greeting=random_greeting)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '')
    response = faq.get_response(user_input)
    # Ensure links are properly formatted
    response = response.replace('[LINK]', '<a').replace('[/LINK]', '</a>')
    return jsonify({'response': response})

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Jewel Changi Assistant</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0056b3;
            --secondary: #003366;
            --accent: #FFD700;
            --light-bg: #f5f7fa;
            --dark-text: #1e293b;
            --ces-blue: #1a73e8;
            --ces-light: #e8f0fe;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: var(--light-bg);
            color: var(--dark-text);
        }
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            height: 100vh;
            display: flex;
            flex-direction: column;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            background: white;
        }
        .chat-header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            position: relative;
            overflow: hidden;
        }
        .chat-header::after {
            content: "✈️";
            position: absolute;
            right: 20px;
            font-size: 40px;
            opacity: 0.2;
            animation: float 3s ease-in-out infinite;
        }
        .logo {
            width: 40px;
            height: 40px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-weight: bold;
        }
        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background-color: rgba(245, 247, 250, 0.95);
            background-image: url('https://www.jewelchangiairport.com/content/dam/jca/common/images/backgrounds/jewel-bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-blend-mode: overlay;
        }
        .message {
            margin-bottom: 15px;
            max-width: 80%;
            animation: fadeIn 0.3s;
        }
        .user-message {
            margin-left: auto;
            background: var(--primary);
            color: white;
            padding: 12px 18px;
            border-radius: 18px 18px 0 18px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transform-origin: right bottom;
            animation: pop 0.2s ease-out;
        }
        .bot-message {
            margin-right: auto;
            background: white;
            padding: 12px 18px;
            border-radius: 18px 18px 18px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transform-origin: left bottom;
            animation: pop 0.2s ease-out;
        }
        .chat-input {
            display: flex;
            padding: 15px;
            background: white;
            border-top: 1px solid #eee;
        }
        #user-input {
            flex: 1;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 25px;
            outline: none;
            font-size: 16px;
            transition: all 0.3s;
        }
        #user-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(0, 86, 179, 0.2);
        }
        #send-button {
            margin-left: 10px;
            padding: 0 20px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #send-button:hover {
            background: var(--secondary);
            transform: scale(1.05);
        }
        .response-box {
            background: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: relative;
            overflow: hidden;
        }
        .response-box::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(to bottom, var(--primary), var(--accent));
        }
        .ces-box {
            background: var(--ces-light);
            border-left: 4px solid var(--ces-blue);
        }
        .ces-box::before {
            background: linear-gradient(to bottom, var(--ces-blue), #8ab4f8);
        }
        .response-box h3 {
            margin-top: 0;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .ces-box h3 {
            color: var(--ces-blue);
        }
        .quick-options {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 15px 0;
        }
        .quick-btn {
            background: var(--light-bg);
            border: 1px solid #ddd;
            border-radius: 20px;
            padding: 8px 15px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .quick-btn:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
            transform: translateY(-2px);
        }
        .ces-btn {
            background: white;
            border: 1px solid var(--ces-blue);
            color: var(--ces-blue);
        }
        .ces-btn:hover {
            background: var(--ces-blue);
            color: white;
            border-color: var(--ces-blue);
        }
        .action-buttons {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        .action-button {
            flex: 1;
            text-align: center;
            background: var(--primary);
            color: white;
            padding: 10px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 14px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }
        .action-button:hover {
            background: var(--secondary);
            transform: translateY(-2px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .ces-action {
            background: var(--ces-blue);
        }
        .ces-action:hover {
            background: #185abc;
        }
        .price-table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 14px;
        }
        .price-table th, .price-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        .price-table th {
            background: var(--light-bg);
            font-weight: 600;
        }
        .ces-table th {
            background: var(--ces-light);
        }
        .deal-banner {
            background: #fff8e6;
            border-left: 4px solid var(--accent);
            padding: 10px;
            margin: 10px 0;
            font-weight: 600;
            border-radius: 4px;
            animation: pulse 2s infinite;
        }
        .ces-banner {
            background: #e8f0fe;
            border-left: 4px solid var(--ces-blue);
            color: var(--ces-blue);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pop {
            0% { transform: scale(0.8); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(255, 215, 0, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); }
        }
        .animation-container {
            height: 60px;
            position: relative;
            margin: 15px 0;
            overflow: hidden;
        }
        .airplane {
            position: absolute;
            font-size: 30px;
            animation: fly 5s linear infinite;
        }
        @keyframes fly {
            0% { left: -50px; transform: rotate(0deg); }
            100% { left: calc(100% + 50px); transform: rotate(10deg); }
        }
        .ces-features {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 10px;
            margin: 15px 0;
        }
        .feature-card {
            background: white;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: all 0.3s;
            border: 1px solid #eee;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .feature-icon {
            font-size: 24px;
            margin-bottom: 5px;
            color: var(--primary);
        }
        .ces-feature .feature-icon {
            color: var(--ces-blue);
        }
        .feature-title {
            font-size: 12px;
            font-weight: 600;
            margin: 5px 0;
        }
        .typing-indicator {
            display: flex;
            padding: 10px 15px;
            background: #f1f1f1;
            border-radius: 20px;
            width: fit-content;
            margin-bottom: 15px;
        }
        .typing-dot {
            width: 8px;
            height: 8px;
            background: #ccc;
            border-radius: 50%;
            margin: 0 2px;
            animation: typing 1.4s infinite ease-in-out;
        }
        .typing-dot:nth-child(1) { animation-delay: 0s; }
        .typing-dot:nth-child(2) { animation-delay: 0.2s; }
        .typing-dot:nth-child(3) { animation-delay: 0.4s; }
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-5px); background: #999; }
        }
        .highlight-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid var(--primary);
        }
        .ces-highlight {
            border-left-color: var(--ces-blue);
            background: linear-gradient(135deg, #e8f0fe 0%, #d2e3fc 100%);
        }
        a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <div class="logo">JC</div>
            <h2>Jewel Changi Assistant</h2>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="message bot-message">
                <div class="response-box">
                    <h3><i class="fas fa-gem"></i> Welcome to Jewel Changi!</h3>
                    <p>{{ random_greeting }}</p>
                    
                    <div class="highlight-card">
                        <h4><i class="fas fa-star"></i> Quick Access</h4>
                        <div class="quick-options">
                            <button class="quick-btn" onclick="askQuestion('opening hours')"><i class="fas fa-clock"></i> Hours</button>
                            <button class="quick-btn" onclick="askQuestion('ticket prices')"><i class="fas fa-ticket-alt"></i> Tickets</button>
                            <button class="quick-btn" onclick="askQuestion('attractions')"><i class="fas fa-map-marked-alt"></i> Attractions</button>
                            <button class="quick-btn" onclick="askQuestion('how to get there')"><i class="fas fa-directions"></i> Directions</button>
                        </div>
                    </div>
                    
                    <div class="highlight-card ces-highlight">
                        <h4><i class="fas fa-vr-cardboard"></i> Changi Experience Studio</h4>
                        <div class="quick-options">
                            <button class="quick-btn ces-btn" onclick="askQuestion('what is changi experience studio')"><i class="fas fa-info-circle"></i> About CES</button>
                            <button class="quick-btn ces-btn" onclick="askQuestion('ces activities')"><i class="fas fa-gamepad"></i> Activities</button>
                            <button class="quick-btn ces-btn" onclick="askQuestion('ces facilities')"><i class="fas fa-wheelchair"></i> Facilities</button>
                            <button class="quick-btn ces-btn" onclick="askQuestion('changi experience studio tickets')"><i class="fas fa-receipt"></i> Tickets</button>
                            <button class="quick-btn ces-btn" onclick="askQuestion('ces operating hours')"><i class="fas fa-calendar-alt"></i> Hours</button>
                            <button class="quick-btn ces-btn" onclick="askQuestion('learning journey')"><i class="fas fa-graduation-cap"></i> School Programs</button>
                        </div>
                    </div>
                    
                    <div class="animation-container">
                        <div class="airplane"><i class="fas fa-plane"></i></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="chat-input">
            <input type="text" id="user-input" placeholder="Ask me anything about Jewel Changi..." autocomplete="off">
            <button id="send-button" onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>

    <script>
        function askQuestion(question) {
            document.getElementById('user-input').value = question;
            sendMessage();
        }
        
        function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();
            
            if (message === '') return;
            
            // Add user message to chat
            addMessage(message, 'user');
            input.value = '';
            
            // Show typing indicator
            const chat = document.getElementById('chat-messages');
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message bot-message';
            typingDiv.innerHTML = '<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
            chat.appendChild(typingDiv);
            chat.scrollTop = chat.scrollHeight;
            
            // Get bot response
            fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                // Remove typing indicator
                chat.removeChild(typingDiv);
                addResponse(data.response);
            })
            .catch(error => {
                console.error('Error:', error);
                chat.removeChild(typingDiv);
                addResponse('<div class="response-box"><h3><i class="fas fa-exclamation-triangle"></i> Error</h3><p>Sorry, something went wrong. Please try again.</p></div>');
            });
        }
        
        function addMessage(message, sender) {
            const chat = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            
            if (sender === 'user') {
                messageDiv.textContent = message;
            } else {
                messageDiv.innerHTML = message;
            }
            
            chat.appendChild(messageDiv);
            chat.scrollTop = chat.scrollHeight;
        }
        
        function addResponse(response) {
            const chat = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot-message';
            messageDiv.innerHTML = response;
            
            chat.appendChild(messageDiv);
            chat.scrollTop = chat.scrollHeight;
            
            // Add animation to any new action buttons
            const buttons = messageDiv.querySelectorAll('.action-button, .quick-btn');
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-2px)';
                });
                button.addEventListener('mouseleave', function() {
                    this.style.transform = '';
                });
            });
        }
        
        // Allow sending message with Enter key
        document.getElementById('user-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        // Focus input on page load
        window.onload = function() {
            document.getElementById('user-input').focus();
        };
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
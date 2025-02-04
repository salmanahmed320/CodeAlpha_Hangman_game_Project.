# CODEALPHA
# Task#3: Basic Chatbot
# Objective: Create a text-based chatbot that can have conversations with users. You can use natural language processing libraries like NLTK or spaCy to make your chatbot more conversational.

# This is a Console Based Chatbot. 
# ******************************* BASIC CHATBOT *****************************************************

import re
import random

# Define pairs for pattern-matching
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! How's it going?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing well. How about you?", "I'm good! Thanks for asking."]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"what do you do ?",
        ["I chat with people and try to help them with their queries.", "I'm here to make your day better by chatting with you."]
    ],
    [
        r"how can you help me ?",
        ["I can provide information, answer simple questions, or just chat with you!", "Try asking me something, and I'll do my best to respond."]
    ],
    [
        r"bye|goodbye|exit",
        ["Goodbye! Have a great day!", "Bye! It was nice talking to you."]
    ],
    [
        r"(.*) created you ?",
        ["I was created by a developer using Python.", "A talented programmer built me using Python and some basic NLP."]
    ],
    [
        r"(.*) (weather|news) ?",
        ["I'm just a chatbot and can't provide live updates. Try a weather or news app!", "I recommend checking a news or weather website for the latest updates."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand that. Can you ask in a different way?", "That's interesting! Tell me more."]
    ]
]

# Function to match user input with responses
def get_response(user_input):
    """
    Matches user input to a pattern and returns a response.
    """
    for pattern, responses in pairs:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return random.choice(responses)
    return "I'm sorry, I didn't understand that."

# Chatbot function
def chatbot():
    print("ChatBot: Hello! I am your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['bye', 'exit', 'goodbye']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

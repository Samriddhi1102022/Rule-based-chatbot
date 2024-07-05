import re
import userInput

def chatbot_response(user_input):
    for pattern, response in userInput.responses.items():
        if re.search(rf"\b{pattern}\b", user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that. Can you rephrase?"


def main():
    print("Welcome to Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
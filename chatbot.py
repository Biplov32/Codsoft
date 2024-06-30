import re

def chatbot_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Pattern matching for predefined responses
    if re.match(r"\b(hello|hi|hey|greetings|howdy|sup)\b", user_input):
        return "Hi there! How can I assist you today?"
    elif re.match(r"\b(goodbye|bye|see you|later|ciao)\b", user_input):
        return "Goodbye! Take care!"
    elif re.match(r"\b(how are you\?|how are you|how's it going|how's life)\b", user_input):
        return "I'm just a chatbot, but I'm here to help you!"
    elif re.match(r"\b(what is your name\?|what is your name|what's your name|who are you)\b", user_input):
        return "I'm a simple, rule-based chatbot here to assist you."
    elif re.match(r"\b(what can you do\?|what do you do|what are your capabilities)\b", user_input):
        return "I can chat with you, answer basic questions, and provide information. What would you like to know?"
    elif re.match(r"\b(tell me a joke|make me laugh|tell me something funny)\b", user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif re.match(r"\b(what's the weather like|what's the weather|weather forecast|weather)\b", user_input):
        return "I can't provide real-time weather updates, but you can check a weather website or app!"
    elif re.match(r"\b(tell me a fun fact|give me a fact|interesting fact)\b", user_input):
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible."
    elif re.match(r"\b(how do you work|how are you made|how are you built)\b", user_input):
        return "I operate based on a set of predefined rules and patterns to respond to your inputs."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hi there! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.match(r"\b(goodbye|bye|see you|later|ciao)\b", user_input.lower()):
            print("Chatbot: Goodbye! Take care!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

chat()

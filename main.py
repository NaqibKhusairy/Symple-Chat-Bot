import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey",["Hello!", "Hey there!", "Hi!"]],
    [r"how are you",["I'm doing well, thank you for asking."]],
    [r"how are you doing|what's your function|what your function|what is your function|your function?",
    ["I'm just a chatbot, but I'm here to help!"]],
    [r"what's your name|what is your name|Your name?|who are you",["I'm a simple chatbot.", "Call me ChatBot."]]
]

def default_response(input_text):
    return "I don't understand what you're talking about."

def handle_pornography(input_text):
    forbidden_words = ["pornography", "adult content", "explicit material", "sexual content","sex"]
    for word in forbidden_words:
        if word in input_text.lower():
            return "Sorry, you mentioned content that I'm not allowed to discuss."
    return None

print("Hi! I'm your simple chatbot \nYou can chat or ask anything to me. Type 'quit' to exit.")
print()
chatbot = Chat(pairs, reflections)
    
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit' or user_input.lower() == 'exit':
        print("Chatbot: Goodbye and see you later!")
        break
    else:
        response = handle_pornography(user_input)
        if response is None:
            response = chatbot.respond(user_input)
            if response is None:
                response = default_response(user_input)
    print("Chatbot:", response)

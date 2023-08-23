import nltk
from nltk.chat.util import Chat, reflections
import os

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"how are you", ["I'm doing well, thank you for asking."]],
    [r"how are you doing|what's your function|what your function|what is your function|your function?",
     ["I'm just a chatbot, but I'm here to help!"]],
    [r"what's your name|what is your name|Your name?|who are you", ["I'm a simple chatbot.", "Call me ChatBot."]],
    [r"tell me a joke|say something funny", ["Why don't scientists trust atoms? Because they make up everything!"]],
    [r"how old are you|your age?", ["I'm ageless, I'm a creation of code!"]],[r"tell me a joke|say something funny", [
        "Sure, here's one: Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Here's a classic: Two atoms bumped into each other. One said, 'I've lost an electron!' The other asked, 'Are you positive?'"]],
    [r"what is the meaning of life", ["The answer to the ultimate question of life, the universe, and everything is 42."]],
    [r"how does the internet work", ["The internet is a global network of interconnected computers that communicate using standardized protocols."]]
]

def default_response(input_text):
    new_response = input("Chatbot: I'm not sure how to respond to that. Please provide an appropriate response: ")
    pairs.append([input_text, [new_response]])
    save_pairs_to_file("custom_responses.txt", [[input_text, [new_response]]])
    print("Chatbot: Thanks for teaching me!")
    return new_response

def handle_pornography(input_text):
    forbidden_words = ["pornography", "adult content", "explicit material", "sexual content", "sex"]
    for word in forbidden_words:
        if word in input_text.lower():
            return "Sorry, you mentioned content that I'm not allowed to discuss."
    return None

def save_pairs_to_file(filename, pairs):
    with open(filename, "a") as file:
        for pair in pairs:
            file.write("Question : " + pair[0] + "\n")
            for response in pair[1]:
                file.write("Response : " + response + "\n")
            file.write("\n")

def load_pairs_from_file(filename):
    loaded_pairs = []
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("Question : "):
                input_pattern = lines[i][11:]
                i += 1
                responses = []
                while i < len(lines) and lines[i].startswith("Response : "):
                    responses.append(lines[i][11:])
                    i += 1
                loaded_pairs.append([input_pattern, responses])
            else:
                i += 1
    return loaded_pairs


print("Hi! I'm your simple chatbot. You can chat or ask anything to me. Type 'quit' to exit.")
print()

while True:
    if not os.path.exists("custom_responses.txt"):
        open("custom_responses.txt", "w").close()
    chatbot = Chat(pairs + load_pairs_from_file("custom_responses.txt"), reflections)
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

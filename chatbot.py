import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')


pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly chatbot.", "They call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I'm good, thanks!", "Doing great. How about you?"]
    ],
    [
        r"Can you help me?",
        ["Sure, I can help you.", "Tell me how I can assist you."]
    ],
    [
        r"Who is your creator?",
        ["I was created by a Python developer for an internship project!"]
    ],
    [
        r"where do you live?",
        ['I am in the cloud, everywhere and nowhere.']
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ]
]


def chatbot():
    print("Hi! I'm ChatBot. Type 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()

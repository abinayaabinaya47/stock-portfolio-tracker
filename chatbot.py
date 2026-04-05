import nltk
from nltk.chat.util import Chat, reflections
import datetime
import webbrowser

pairs = [
    [r"hi|hello|hey", ["Hello 👋", "Hi there!"]],
    [r"what is your name ?", ["I am SmartBot 🤖"]],
    [r"how are you ?", ["I'm doing great!"]],
    [r"your name", ["You can call me SmartBot"]],
    [r"help", ["I can help you with time, date, Google search, and chatting!"]],
]

chat = Chat(pairs, reflections)

print("🤖 Smart Chatbot (type 'quit' to exit)")

while True:
    user = input("You: ").lower()

    if user == "quit":
        print("Bot: Goodbye 👋")
        break

    # 🔹 Feature 1: Time
    elif "time" in user:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", now)

    # 🔹 Feature 2: Date
    elif "date" in user:
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    # 🔹 Feature 3: Google Search
    elif "search" in user:
        query = user.replace("search", "")
        print("Bot: Searching for", query)
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # 🔹 Feature 4: Calculator
    elif "calculate" in user:
        try:
            expr = user.replace("calculate", "")
            result = eval(expr)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid calculation")

    # 🔹 NLP response
    else:
        response = chat.respond(user)
        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I don't understand 🤔")
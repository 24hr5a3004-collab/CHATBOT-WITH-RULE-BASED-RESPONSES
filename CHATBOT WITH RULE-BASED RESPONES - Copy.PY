# Simple Rule-Based Chatbot

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hi there!")

    elif "how are you" in user:
        print("Chatbot: I am fine. Thank you!")

    elif "your name" in user:
        print("Chatbot: I am a Rule-Based Chatbot.")

    elif "help" in user:
        print("Chatbot: I can answer simple questions.")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
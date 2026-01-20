print("Welcome to Medhamsh's AI Chatbot!")

while True:
    user = input("\nYou: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")
    elif "how are you" in user:
        print("Bot: I'm just code, but I'm doing great!")
    elif "bye" in user:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")

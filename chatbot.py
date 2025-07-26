print("Welcome to the chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you today?")
    elif user_input == "how are you":
        print("Bot: I'm just a bot, but I'm doing great! Thanks for asking.")
    elif user_input == "what is your name":
        print("Bot: I'm ChatBot 101, your Python assistant!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
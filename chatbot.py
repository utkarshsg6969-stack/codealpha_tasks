def chatbot():

    print("===================================")
    print("         SIMPLE CHATBOT            ")
    print("===================================")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower()

        # Greetings
        if user_input == "hello":
            print("Bot: Hi there!")

        elif user_input == "hi":
            print("Bot: Hello!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thank you!")

        elif user_input == "your name":
            print("Bot: I am a Python Chatbot.")

        elif user_input == "what can you do":
            print("Bot: I can respond to simple messages.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()

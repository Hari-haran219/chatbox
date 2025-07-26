def get_bot_response(user_input):
    responses = {
        "hello": "Hi!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!",
        "what's your name": "I'm a simple chatbot."
    }

    # Normalize input
    user_input = user_input.lower()

    # Return response if known, else default
    return responses.get(user_input, "Sorry, I don't understand that.")

def chatbot():
    print("Chatbot: Hi! Let's chat. Type 'bye' to end.\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == "bye":
            break

# Run the chatbot
chatbot()

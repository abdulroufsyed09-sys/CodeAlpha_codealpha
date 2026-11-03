def chatbot_reply(message):
    message = message.lower()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I am a simple chatbot."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


print("Chatbot started. Type 'bye' to exit.")

while True:
    user = input("You: ")
    reply = chatbot_reply(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break
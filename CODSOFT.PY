def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, but thanks for asking!"
    elif "weather" in user_input.lower():
        return "Sorry, I can't provide weather updates at the moment."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Test the chatbot
while True:
    user_query = input("You: ")
    if user_query.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_query)
    print("Chatbot:", response)

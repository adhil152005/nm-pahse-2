
# Simple rule-based chatbot
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "problem" in user_input:
        return "I'm sorry to hear that. Can you please provide more details?"
    elif "price" in user_input:
        return "Our pricing details are available on the website. Would you like the link?"
    else:
        return "I'm not sure I understand. Could you please rephrase?"

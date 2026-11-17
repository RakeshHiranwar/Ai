# Banking Enquiry Chatbot

print("Welcome to Banking Enquiry Chatbot!")
print("You can ask about balance, account, loans, ATM, and services.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    # Predefined rules and pattern matching

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "balance" in user:
        print("Bot: You can check your account balance using mobile banking or ATM.")

    elif "account" in user:
        print("Bot: You can open a savings or current account at our bank.")

    elif "loan" in user:
        print("Bot: We provide home loans, education loans and personal loans.")

    elif "atm" in user:
        print("Bot: Our ATM services are available 24/7.")

    elif "interest" in user:
        print("Bot: Interest rates depend on the type of account or loan.")

    elif "credit card" in user:
        print("Bot: You can apply for a credit card through our bank website.")

    elif "ifsc" in user:
        print("Bot: You can find the IFSC code on your cheque book or bank website.")

    elif "working hours" in user or "timing" in user:
        print("Bot: Our bank working hours are 10 AM to 4 PM.")

    elif "bye" in user:
        print("Bot: Thank you for contacting our bank. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand your question.")
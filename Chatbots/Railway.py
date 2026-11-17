# Railway Enquiry Chatbot

print("Welcome to Railway Enquiry Chatbot!")
print("You can ask about trains, timings, tickets, and platforms.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    # Predefined rules and pattern matching

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "train" in user:
        print("Bot: We have express, passenger and superfast trains.")

    elif "timing" in user:
        print("Bot: Please check the railway enquiry counter for train timings.")

    elif "ticket" in user or "booking" in user:
        print("Bot: You can book tickets online through IRCTC or at the railway counter.")

    elif "platform" in user:
        print("Bot: Please check the station display board for platform information.")

    elif "fare" in user or "price" in user:
        print("Bot: Ticket fare depends on the train and travel distance.")

    elif "pnr" in user or "status" in user:
        print("Bot: You can check your PNR status on the IRCTC website.")

    elif "cancel" in user:
        print("Bot: You can cancel your ticket online or at the railway reservation counter.")

    elif "bye" in user:
        print("Bot: Thank you for using Railway Enquiry Chatbot. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand your question.")
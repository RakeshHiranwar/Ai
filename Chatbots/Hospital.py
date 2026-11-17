# Hospital Enquiry Chatbot

print("Welcome to Hospital Enquiry Chatbot!")
print("You can ask about doctors, timings, appointments, and services.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    # Predefined rules and pattern matching

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "doctor" in user:
        print("Bot: Our hospital has specialist doctors in different departments.")

    elif "timing" in user:
        print("Bot: Hospital is open from 9 AM to 8 PM.")

    elif "appointment" in user:
        print("Bot: You can book an appointment at the hospital reception.")

    elif "emergency" in user:
        print("Bot: Our emergency department is available 24/7.")

    elif "department" in user:
        print("Bot: We have Cardiology, Neurology, Orthopedics and Pediatrics departments.")

    elif "address" in user or "location" in user:
        print("Bot: Our hospital is located in Pune.")

    elif "fee" in user or "charges" in user:
        print("Bot: Please contact the reception for consultation fees.")

    elif "bye" in user:
        print("Bot: Thank you for contacting us. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand your question.")
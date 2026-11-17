# College Enquiry Chatbot

print("Welcome to College Enquiry Chatbot!")
print("You can ask about courses, fees, admission, and timings.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    # Predefined rules and pattern matching

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "course" in user:
        print("Bot: We offer Computer, IT, Mechanical, and Civil Engineering.")

    elif "admission" in user:
        print("Bot: Admissions are based on entrance exam scores.")

    elif "fee" in user:
        print("Bot: Please contact the college office for fee details.")

    elif "timing" in user:
        print("Bot: College timing is 9 AM to 5 PM.")

    elif "location" in user or "address" in user:
        print("Bot: Our college is located in Pune.")

    elif "placement" in user:
        print("Bot: Our college provides placement assistance to students.")

    elif "bye" in user:
        print("Bot: Thank you for contacting us. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand your question.")
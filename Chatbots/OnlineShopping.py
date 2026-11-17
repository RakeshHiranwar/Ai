# Online Shopping Assistant Chatbot

print("Welcome to Online Shopping Assistant!")
print("You can ask about products, prices, orders, delivery, and returns.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    # Predefined rules and pattern matching

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "product" in user:
        print("Bot: We have mobiles, laptops, clothes and accessories.")

    elif "price" in user:
        print("Bot: Product prices are available on our website.")

    elif "order" in user:
        print("Bot: You can place an order by adding products to your cart.")

    elif "delivery" in user:
        print("Bot: Delivery usually takes 3-5 business days.")

    elif "payment" in user:
        print("Bot: We accept UPI, credit cards, debit cards and cash on delivery.")

    elif "return" in user:
        print("Bot: Products can be returned within 7 days of delivery.")

    elif "cancel" in user:
        print("Bot: You can cancel your order from the My Orders section.")

    elif "discount" in user or "offer" in user:
        print("Bot: We provide special discounts during festival sales.")

    elif "bye" in user:
        print("Bot: Thank you for shopping with us. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand your question.")   
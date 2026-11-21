import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "faq.json")

faq_data = {
    "products": {
        "price": "Our product prices start from $10.",
        "delivery": "We provide delivery within 3-5 working days.",
        "payment": "We accept cash, credit cards, and online payments.",
        "return": "Products can be returned within 7 days of purchase.",
    }
}


def load_faqs() -> dict:
    try:
        if not os.path.exists(FAQ_FILE):
            with open(FAQ_FILE, "w", encoding="utf-8") as file:
                json.dump(faq_data, file, indent=4)

        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return faq_data


FAQS = load_faqs()


def get_response(user_input: str) -> list[str]:
    message = user_input.lower().strip()
    responses = []

    if re.search(r"\b(hello|hi|hey|good morning|good evening)\b", message):
        responses.append("Hello! Welcome to our customer support chatbot. How can I help you?")

    if re.search(r"\b(hours|open|opening|closing|time|working hours)\b", message):
        responses.append("Our business hours are Monday to Friday, 9 AM to 5 PM.")

    if re.search(r"\b(price|cost|prices|how much)\b", message):
        responses.append(FAQS["products"]["price"])

    if re.search(r"\b(delivery|shipping|deliver)\b", message):
        responses.append(FAQS["products"]["delivery"])

    if re.search(r"\b(payment|pay|cash|card)\b", message):
        responses.append(FAQS["products"]["payment"])

    if re.search(r"\b(return|refund|exchange)\b", message):
        responses.append(FAQS["products"]["return"])

    if not responses:
        responses.append(
            "Sorry, I didn't understand that. Please ask about business hours, prices, delivery, payment, or returns."
        )

    return responses


def chatbot() -> None:
    print("======================================")
    print("       CUSTOMER SUPPORT CHATBOT")
    print("======================================")
    print("Bot: Hello! How can I help you?")
    print("Bot: Type 'bye', 'exit', or 'quit' to leave.")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        if re.search(r"\b(bye|exit|quit)\b", user_input, re.IGNORECASE):
            print("Bot: Thank you for contacting us. Goodbye!")
            break

        try:
            for response in get_response(user_input):
                print("Bot:", response)
        except (KeyError, TypeError):
            print("Bot: Sorry, something went wrong. Please try again.")


if __name__ == "__main__":
    chatbot()
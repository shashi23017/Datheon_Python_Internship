# Task 4 – Rule-Based Interactive Terminal Assistant / Chatbot

## Project Description

This project is a rule-based interactive customer support chatbot developed using Python. It allows users to ask questions about business hours, product prices, delivery, payment methods, and return policies.

The chatbot uses regular expressions to recognize user intents and provides relevant responses. It also supports multiple-intent matching, fallback responses, and exit commands.

## Features

- Interactive terminal-based conversation.
- Greeting recognition.
- Business hours information.
- Product price information.
- Delivery information.
- Payment method information.
- Return and refund policy information.
- Multiple-intent recognition.
- Fallback responses for unknown questions.
- Exit commands (`bye`, `exit`, `quit`).
- FAQ data stored in a JSON file.
- Basic error handling.

## Technologies Used

- Python 3
- JSON
- Regular Expressions (`re`)
- OS Module
- Functions
- Lists and Dictionaries
- Exception Handling

## Project Structure

```text
Task4/
│
├── chatbot.py
├── faq.json
└── README.md
```

## How to Run

1. Open the Task4 folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python chatbot.py
```

## How It Works

1. The chatbot loads FAQ information from `faq.json`.
2. The user enters a message in the terminal.
3. The chatbot converts the message into lowercase.
4. Regular expressions identify keywords and user intents.
5. The chatbot provides relevant responses.
6. If the message contains multiple intents, it provides multiple responses.
7. If the chatbot cannot recognize the message, it displays a fallback response.
8. The user can type `bye`, `exit`, or `quit` to end the conversation.

## Sample Conversation

```text
======================================
       CUSTOMER SUPPORT CHATBOT
======================================
Bot: Hello! How can I help you?
Bot: Type 'bye', 'exit', or 'quit' to leave.

You: Hi
Bot: Hello! Welcome to our customer support chatbot. How can I help you?

You: What are your business hours?
Bot: Our business hours are Monday to Friday, 9 AM to 5 PM.

You: Tell me the delivery time
Bot: We provide delivery within 3-5 working days.

You: What is the price and payment method?
Bot: Our product prices start from $10.
Bot: We accept cash, credit cards, and online payments.

You: bye
Bot: Thank you for contacting us. Goodbye!
```

## Learning Outcomes

- Understanding Python regular expressions.
- Working with JSON files.
- Recognizing multiple user intents.
- Developing interactive terminal applications.
- Using functions and loops.
- Handling errors and unexpected inputs.

## Author

Datheon Python Programming Internship – Task 4

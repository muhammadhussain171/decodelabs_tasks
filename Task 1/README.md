# Rule-Based AI Chatbot

## Project Overview

The Rule-Based AI Chatbot is a Python-based conversational program that responds to user messages using predefined rules.

Unlike machine learning chatbots, this system does not require model training or an external AI API. It identifies keywords and patterns in the user's input and selects an appropriate response.

## Features

- Greeting detection
- Basic conversation
- AI-related questions
- Python-related questions
- Current date and time
- Help command
- Thank-you responses
- Goodbye responses
- Unknown-input handling
- Interactive command-line interface

## How It Works

The chatbot follows a simple rule-based process:

1. The user enters a message.
2. The message is converted to lowercase.
3. The program checks the message against predefined rules.
4. Matching keywords or phrases trigger a suitable response.
5. If no rule matches, the chatbot provides a default response.
6. The conversation continues until the user enters `exit`, `quit`, or `q`.

## Technologies Used

- Python
- Rule-Based Artificial Intelligence
- Natural Language Processing concepts
- `random`
- `datetime`

## Project Structure

```text
Task 1/
│
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
````

## Installation

Python 3.x is required.

No external Python packages are required for this project.

Run:

```bash
python chatbot.py
```

## Example Conversation

```text
RULE-BASED AI CHATBOT

Hello! I'm DecoBot.

You: hello
DecoBot: Hello! I'm DecoBot. How can I help you?

You: who are you
DecoBot: I'm DecoBot, a rule-based AI chatbot created using Python.

You: what is AI
DecoBot: AI stands for Artificial Intelligence. It enables computers
to perform tasks that normally require human intelligence.

You: what time is it
DecoBot: The current time is 10:30:25 AM.

You: exit
DecoBot: Goodbye! Thanks for chatting.
```

## Limitations

Because the chatbot is rule-based, it can only respond to patterns that have been explicitly programmed.

It does not understand the meaning or intent of completely new questions like a modern large language model.

## Future Improvements

Possible improvements include:

* Adding more conversational rules
* Using NLP for intent detection
* Adding a graphical user interface
* Adding speech recognition
* Connecting the chatbot to a machine learning model

## Author

Maheen Kanwal

## Internship Project

This project was developed as part of an Artificial Intelligence internship.

````

### Project 1 is now complete

```text
Task 1/
│
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
````

### Step 4 — Final test

Run:

```powershell
python chatbot.py
```

Test these one by one:

```text
hello
who are you
what can you do
what is AI
what is Python
what time is it
thank you
exit
```
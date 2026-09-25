import random
from datetime import datetime


# ================================================================
# RULE-BASED AI CHATBOT
# ================================================================

BOT_NAME = "DecoBot"


def get_response(user_input):
    """Generate a response using predefined rules."""

    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in [
        "hello",
        "hi",
        "hey",
        "salam",
        "assalamualaikum"
    ]):
        responses = [
            f"Hello! I'm {BOT_NAME}. How can I help you?",
            f"Hi there! I'm {BOT_NAME}. What can I do for you?",
            "Hello! Nice to meet you."
        ]

        return random.choice(responses)

    # How are you
    elif "how are you" in text:
        return "I'm doing great! Thanks for asking."

    # Bot identity
    elif (
        "who are you" in text
        or "your name" in text
        or "what are you" in text
    ):
        return (
            f"I'm {BOT_NAME}, a rule-based AI chatbot "
            "created using Python."
        )

    # Creator
    elif (
        "who created you" in text
        or "who made you" in text
        or "your creator" in text
    ):
        return (
            "I was created as an Artificial Intelligence "
            "internship project."
        )

    # Help
    elif "help" in text:
        return (
            "I can respond to greetings, tell you the "
            "current date and time, explain what I am, "
            "and answer some basic questions."
        )

    # Date
    elif (
        "date" in text
        or "today" in text
        or "what day" in text
    ):
        current_date = datetime.now().strftime(
            "%A, %d %B %Y"
        )

        return f"Today's date is {current_date}."

    # Time
    elif "time" in text:
        current_time = datetime.now().strftime(
            "%I:%M:%S %p"
        )

        return f"The current time is {current_time}."

    # Thanks
    elif any(word in text for word in [
        "thank you",
        "thanks",
        "thx"
    ]):
        return "You're welcome! I'm happy to help."

    # Goodbye
    elif any(word in text for word in [
        "bye",
        "goodbye",
        "see you"
    ]):
        return "Goodbye! Have a great day."

    # Basic questions
    elif "what can you do" in text:
        return (
            "I can have simple conversations using "
            "predefined rules and responses."
        )

    elif "ai" in text:
        return (
            "AI stands for Artificial Intelligence. "
            "It enables computers to perform tasks "
            "that normally require human intelligence."
        )

    elif "python" in text:
        return (
            "Python is a popular programming language "
            "widely used in AI, data science, automation, "
            "and software development."
        )

    # Unknown input
    else:
        return (
            "I'm sorry, I don't understand that yet. "
            "Try asking for help or using a different question."
        )


def chatbot():

    print("=" * 65)
    print("              RULE-BASED AI CHATBOT")
    print("=" * 65)

    print(
        f"\nHello! I'm {BOT_NAME}."
    )

    print(
        "Type 'help' to see what I can do."
    )

    print(
        "Type 'exit' or 'quit' to end the conversation."
    )

    print("-" * 65)

    while True:

        user_input = input(
            "\nYou: "
        ).strip()

        if not user_input:
            print(
                f"{BOT_NAME}: Please enter a message."
            )
            continue

        if user_input.lower() in [
            "exit",
            "quit",
            "q"
        ]:
            print(
                f"{BOT_NAME}: Goodbye! Thanks for chatting."
            )
            break

        response = get_response(
            user_input
        )

        print(
            f"{BOT_NAME}: {response}"
        )


if __name__ == "__main__":
    chatbot()
import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# ================================================================
# AI SPAM EMAIL CLASSIFIER
# ================================================================

DATA_FILE = "emails.csv"


def clean_text(text):
    """Clean email text before machine learning processing."""

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def load_dataset():
    """Load and validate the email dataset."""

    file_path = Path(DATA_FILE)

    if not file_path.exists():
        print(f"\nError: {DATA_FILE} was not found.")
        return None

    try:
        data = pd.read_csv(file_path)

        required_columns = ["label", "text"]

        if not all(
            column in data.columns
            for column in required_columns
        ):
            print(
                "\nError: Dataset must contain "
                "'label' and 'text' columns."
            )
            return None

        data = data.dropna(
            subset=["label", "text"]
        )

        data["text"] = data["text"].apply(
            clean_text
        )

        return data

    except Exception as error:
        print(
            f"\nError loading dataset: {error}"
        )
        return None


def train_model(data):
    """Train the spam classification model."""

    print("\nPreparing training data...")

    X = data["text"]
    y = data["label"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.25,
            random_state=42,
            stratify=y
        )
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                stop_words="english",
                max_features=5000
            )
        ),
        (
            "classifier",
            MultinomialNB()
        )
    ])

    print("Training AI model...")

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return (
        model,
        accuracy,
        y_test,
        predictions
    )


def display_model_results(
    accuracy,
    y_test,
    predictions
):
    """Display model performance."""

    print("\n" + "=" * 70)
    print("MODEL PERFORMANCE")
    print("=" * 70)

    print(
        f"\nModel Accuracy: "
        f"{accuracy * 100:.2f}%"
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )


def predict_email(model, email_text):
    """Predict whether an email is spam or not spam."""

    cleaned_email = clean_text(
        email_text
    )

    prediction = model.predict(
        [cleaned_email]
    )[0]

    probabilities = model.predict_proba(
        [cleaned_email]
    )[0]

    confidence = max(
        probabilities
    ) * 100

    return prediction, confidence


def interactive_prediction(model):
    """Allow the user to test custom emails."""

    print("\n" + "=" * 70)
    print("TEST A CUSTOM EMAIL")
    print("=" * 70)

    print(
        "\nEnter an email message to classify."
    )

    print(
        "Type 'exit' to close the program."
    )

    while True:

        email_text = input(
            "\nEmail text: "
        ).strip()

        if email_text.lower() == "exit":

            print(
                "\nProgram closed successfully."
            )
            break

        if not email_text:

            print(
                "Please enter an email message."
            )
            continue

        prediction, confidence = (
            predict_email(
                model,
                email_text
            )
        )

        print("\n" + "-" * 50)

        if prediction.lower() == "spam":

            print("Prediction: SPAM ⚠")

        else:

            print("Prediction: NOT SPAM ✓")

        print(
            f"Confidence: "
            f"{confidence:.2f}%"
        )

        print("-" * 50)


def main():

    print("=" * 70)
    print("AI SPAM EMAIL CLASSIFIER")
    print("=" * 70)

    print(
        "\nLoading email dataset..."
    )

    data = load_dataset()

    if data is None:
        return

    print(
        "Dataset loaded successfully!"
    )

    print(
        f"Total emails: "
        f"{len(data)}"
    )

    print(
        f"Spam emails: "
        f"{sum(data['label'].str.lower() == 'spam')}"
    )

    print(
        f"Not spam emails: "
        f"{sum(data['label'].str.lower() == 'ham')}"
    )

    (
        model,
        accuracy,
        y_test,
        predictions
    ) = train_model(data)

    display_model_results(
        accuracy,
        y_test,
        predictions
    )

    interactive_prediction(
        model
    )


if __name__ == "__main__":
    main()
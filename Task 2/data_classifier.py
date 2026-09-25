import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


# ================================================================
# DATA CLASSIFICATION SYSTEM
# ================================================================

DATA_FILE = "data.csv"


def load_dataset():
    """Load and validate the dataset."""

    try:
        data = pd.read_csv(DATA_FILE)

    except FileNotFoundError:
        print(f"\nError: {DATA_FILE} was not found.")
        return None

    required_columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        print(
            "\nError: Missing columns:",
            missing_columns
        )
        return None

    data = data.dropna()

    return data


def train_classifier(data):
    """Train the K-Nearest Neighbors classifier."""

    features = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]

    X = data[features]
    y = data["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(
        n_neighbors=5
    )

    model.fit(
        X_train_scaled,
        y_train
    )

    predictions = model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return (
        model,
        scaler,
        accuracy,
        y_test,
        predictions
    )


def display_results(
    accuracy,
    y_test,
    predictions
):
    """Display model performance."""

    print("\n" + "=" * 70)
    print("MODEL PERFORMANCE")
    print("=" * 70)

    print(
        f"\nAccuracy: {accuracy * 100:.2f}%"
    )

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )


def predict_custom_flower(
    model,
    scaler
):
    """Predict a flower from user-provided measurements."""

    print("\n" + "=" * 70)
    print("CUSTOM DATA CLASSIFICATION")
    print("=" * 70)

    try:
        sepal_length = float(
            input("Sepal length: ")
        )

        sepal_width = float(
            input("Sepal width: ")
        )

        petal_length = float(
            input("Petal length: ")
        )

        petal_width = float(
            input("Petal width: ")
        )

    except ValueError:
        print(
            "\nError: Please enter numerical values."
        )
        return

    sample = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    sample_scaled = scaler.transform(
        sample
    )

    prediction = model.predict(
        sample_scaled
    )

    print("\n" + "-" * 70)
    print("PREDICTION")
    print("-" * 70)

    print(
        f"\nPredicted class: {prediction[0]}"
    )


def main():

    print("=" * 70)
    print("                 DATA CLASSIFICATION SYSTEM")
    print("=" * 70)

    print("\nLoading dataset...")

    data = load_dataset()

    if data is None:
        return

    print(
        "Dataset loaded successfully!"
    )

    print(
        f"Total records: {len(data)}"
    )

    print(
        f"Number of classes: "
        f"{data['species'].nunique()}"
    )

    print(
        "\nClasses:"
    )

    for species in sorted(
        data["species"].unique()
    ):
        print(
            f"  - {species}"
        )

    print(
        "\nTraining classification model..."
    )

    (
        model,
        scaler,
        accuracy,
        y_test,
        predictions
    ) = train_classifier(data)

    print(
        "Model trained successfully!"
    )

    display_results(
        accuracy,
        y_test,
        predictions
    )

    predict_custom_flower(
        model,
        scaler
    )

    print("\n" + "=" * 70)
    print("             CLASSIFICATION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()
import os
from pathlib import Path

from PIL import Image
from transformers import pipeline


# ================================================================
# AI IMAGE RECOGNITION SYSTEM
# ================================================================

IMAGE_FOLDER = "images"
TOP_PREDICTIONS = 5


def load_model():
    """Load the pre-trained AI image classification model."""

    print("\nLoading pre-trained AI model...")
    print("Please wait...")

    try:
        classifier = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        )

        print("Model loaded successfully!")

        return classifier

    except Exception as error:
        print(f"\nError loading AI model: {error}")
        return None


def get_image_files():
    """Get all supported images from the images folder."""

    image_folder = Path(IMAGE_FOLDER)

    if not image_folder.exists():
        print(f"\nCreating '{IMAGE_FOLDER}' folder...")
        image_folder.mkdir()
        return []

    supported_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    )

    image_files = [
        file
        for file in image_folder.iterdir()
        if file.suffix.lower() in supported_extensions
    ]

    return image_files


def analyze_image(classifier, image_path):
    """Analyze a single image."""

    try:
        image = Image.open(image_path).convert("RGB")

        print(f"\nImage: {image_path.name}")
        print(f"Size: {image.size[0]} x {image.size[1]}")

        predictions = classifier(
            image,
            top_k=TOP_PREDICTIONS
        )

        return predictions

    except Exception as error:
        print(f"\nError analyzing {image_path.name}: {error}")
        return None


def get_confidence_assessment(score):
    """Return a confidence assessment."""

    percentage = score * 100

    if percentage >= 80:
        return "Very High Confidence"

    elif percentage >= 60:
        return "High Confidence"

    elif percentage >= 40:
        return "Moderate Confidence"

    else:
        return "Low Confidence"


def display_predictions(predictions):
    """Display predictions."""

    if not predictions:
        return

    best_prediction = predictions[0]

    print("\n" + "-" * 65)
    print("BEST PREDICTION")
    print("-" * 65)

    print(
        f"Prediction : "
        f"{best_prediction['label']}"
    )

    print(
        f"Confidence : "
        f"{best_prediction['score'] * 100:.2f}%"
    )

    print(
        f"Assessment : "
        f"{get_confidence_assessment(best_prediction['score'])}"
    )

    print("\nTOP 5 PREDICTIONS")
    print("-" * 65)

    for number, prediction in enumerate(
        predictions,
        start=1
    ):

        label = prediction["label"]
        confidence = prediction["score"] * 100

        print(
            f"{number}. "
            f"{label:<40} "
            f"{confidence:.2f}%"
        )


def main():

    print("=" * 70)
    print("AI IMAGE RECOGNITION SYSTEM")
    print("=" * 70)

    classifier = load_model()

    if classifier is None:
        return

    print("\nChecking image folder...")

    image_files = get_image_files()

    if not image_files:

        print("\nNo images found.")

        print(
            f"Please add images to the "
            f"'{IMAGE_FOLDER}' folder."
        )

        return

    print(
        f"Images available: "
        f"{len(image_files)}"
    )

    successful_analyses = 0

    # Analyze every image
    for image_path in image_files:

        print("\n" + "=" * 70)
        print("ANALYZING IMAGE")
        print("=" * 70)

        predictions = analyze_image(
            classifier,
            image_path
        )

        if predictions:

            display_predictions(
                predictions
            )

            successful_analyses += 1

    # Final summary
    print("\n" + "=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)

    print(
        f"\nTotal images found: "
        f"{len(image_files)}"
    )

    print(
        f"Successfully analyzed: "
        f"{successful_analyses}"
    )

    print(
        f"Failed analyses: "
        f"{len(image_files) - successful_analyses}"
    )

    print(
        "\nAI Image Recognition System "
        "completed successfully!"
    )

    print("=" * 70)


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================

if __name__ == "__main__":
    main()
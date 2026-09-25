import pandas as pd
from pathlib import Path


# ================================================================
# AI BOOK RECOMMENDATION SYSTEM
# ================================================================

DATA_FILE = "books.csv"


def load_dataset():
    """Load the book dataset."""

    file_path = Path(DATA_FILE)

    if not file_path.exists():
        print(f"\nError: '{DATA_FILE}' was not found.")
        print("Please make sure books.csv is in the project folder.")
        return None

    try:
        data = pd.read_csv(file_path)

        required_columns = [
            "title",
            "author",
            "genres",
            "rating",
            "ratings_count"
        ]

        for column in required_columns:
            if column not in data.columns:
                print(f"\nError: Missing required column: {column}")
                return None

        return data

    except Exception as error:
        print(f"\nError loading dataset: {error}")
        return None


def get_user_preferences():
    """Get preferred book genres from the user."""

    print("\n" + "=" * 70)
    print("USER PREFERENCES")
    print("=" * 70)

    print("\nExamples:")
    print("Fantasy, Mystery, Romance")
    print("Science Fiction, Adventure")
    print("History, Biography")

    preferences = input(
        "\nEnter your preferred genres (separated by commas): "
    ).strip()

    if not preferences:
        return []

    preference_list = [
        genre.strip().lower()
        for genre in preferences.split(",")
        if genre.strip()
    ]

    return preference_list


def calculate_genre_match(book_genres, user_preferences):
    """Calculate how well a book matches user preferences."""

    book_genre_list = [
        genre.strip().lower()
        for genre in str(book_genres).split("|")
    ]

    if not user_preferences:
        return 0

    matched_genres = 0

    for preference in user_preferences:
        if preference in book_genre_list:
            matched_genres += 1

    match_percentage = (
        matched_genres / len(user_preferences)
    ) * 100

    return match_percentage


def normalize_ratings(data):
    """Normalize rating values to a score out of 100."""

    max_rating = 5

    return (data["rating"] / max_rating) * 100


def calculate_popularity_score(data):
    """Calculate popularity score based on number of ratings."""

    maximum = data["ratings_count"].max()

    if maximum == 0:
        return pd.Series([0] * len(data))

    return (
        data["ratings_count"] / maximum
    ) * 100


def recommend_books(data, preferences, top_n=10):
    """Generate book recommendations."""

    recommendation_data = data.copy()

    # Calculate genre match
    recommendation_data["genre_match"] = (
        recommendation_data["genres"].apply(
            lambda genres: calculate_genre_match(
                genres,
                preferences
            )
        )
    )

    # Rating score
    recommendation_data["rating_score"] = (
        normalize_ratings(recommendation_data)
    )

    # Popularity score
    recommendation_data["popularity_score"] = (
        calculate_popularity_score(
            recommendation_data
        )
    )

    # Final recommendation score
    recommendation_data["final_score"] = (
        recommendation_data["genre_match"] * 0.60
        + recommendation_data["rating_score"] * 0.30
        + recommendation_data["popularity_score"] * 0.10
    )

    # Keep only books that match at least one preference
    matched_books = recommendation_data[
        recommendation_data["genre_match"] > 0
    ]

    # Sort by final recommendation score
    recommendations = matched_books.sort_values(
        by="final_score",
        ascending=False
    )

    return recommendations.head(top_n), matched_books


def display_recommendations(recommendations):
    """Display recommended books."""

    print("\n" + "=" * 70)
    print("TOP 10 BOOK RECOMMENDATIONS")
    print("=" * 70)

    if recommendations.empty:
        print("\nNo matching books found.")
        print("Try entering different genres.")
        return

    for index, (_, book) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        print(f"\n{index}. {book['title']}")

        print(f"   Author: {book['author']}")

        print(f"   Genres: {book['genres']}")

        print(
            f"   Average Rating: "
            f"{book['rating']:.2f}/5"
        )

        print(
            f"   Number of Ratings: "
            f"{int(book['ratings_count']):,}"
        )

        print(
            f"   Genre Match: "
            f"{book['genre_match']:.0f}%"
        )

        print(
            f"   Final Recommendation Score: "
            f"{book['final_score']:.2f}/100"
        )


def display_summary(data, matched_books, recommendations):
    """Display project summary."""

    print("\n" + "=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)

    print(f"\nBooks in dataset: {len(data)}")

    print(
        f"Books matching preferences: "
        f"{len(matched_books)}"
    )

    print(
        f"Recommendations displayed: "
        f"{len(recommendations)}"
    )

    print("\nScoring Method:")

    print("60% User Preference Match")
    print("30% Average Book Rating")
    print("10% Book Popularity")

    print(
        "\nAI Book Recommendation System "
        "completed successfully!"
    )

    print("=" * 70)


def main():

    print("=" * 70)
    print("AI BOOK RECOMMENDATION SYSTEM")
    print("=" * 70)

    print("\nLoading book dataset...")

    data = load_dataset()

    if data is None:
        return

    print("Dataset loaded successfully!")

    print(
        f"Total books available: "
        f"{len(data)}"
    )

    # Get user preferences
    preferences = get_user_preferences()

    if not preferences:

        print("\nNo preferences entered.")
        print("Program ended.")

        return

    print("\nYour selected preferences:")

    for preference in preferences:
        print(
            f"  - {preference.title()}"
        )

    # Generate recommendations
    recommendations, matched_books = recommend_books(
        data,
        preferences
    )

    # Display results
    display_recommendations(
        recommendations
    )

    display_summary(
        data,
        matched_books,
        recommendations
    )


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================

if __name__ == "__main__":
    main()
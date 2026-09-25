# AI Book Recommendation System

## Project Overview

The AI Book Recommendation System is a Python-based recommendation project that suggests books according to the user's preferred genres.

The system analyzes a dataset containing book titles, authors, genres, ratings, and popularity information. It calculates a recommendation score and displays the top matching books.

---

## Features

- User-based genre preferences
- Book genre matching
- Average rating analysis
- Popularity analysis
- Recommendation scoring
- Top 10 book recommendations
- Large book dataset
- Clean console interface

---

## How the Recommendation System Works

The user enters one or more preferred genres.

Example:

```text
Fantasy, Adventure, Mystery
````

The system analyzes every book in the dataset and calculates:

* Genre Match Score
* Rating Score
* Popularity Score

The final recommendation score is calculated using:

```text
60% Genre Match
30% Average Rating
10% Popularity
```

Books with the highest final scores are displayed as recommendations.

---

## Dataset

The dataset is stored in:

```text
books.csv
```

It contains the following information:

* Book Title
* Author
* Genres
* Average Rating
* Number of Ratings

---

## Technologies Used

* Python
* Pandas
* Recommendation Logic
* Data Analysis

---

## Installation

Clone the repository or download the project files.

Install the required library:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the program using:

```bash
python recommendation.py
```

Then enter your preferred genres.

Example:

```text
Enter your preferred genres: Fantasy, Adventure, Mystery
```

The program will display the top 10 recommended books.

---

## Project Structure

```text
Project 3 - AI Book Recommendation System/
│
├── recommendation.py
├── books.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Example Output

```text
AI BOOK RECOMMENDATION SYSTEM

Enter your preferred genres:
Fantasy, Adventure

TOP 10 BOOK RECOMMENDATIONS

1. Words of Radiance
   Author: Brandon Sanderson
   Genres: Fantasy|Adventure|Epic
   Average Rating: 4.76/5
   Genre Match: 100%
   Final Recommendation Score: 91.56/100
```

---

## Author

Maheen Kanwal

---

## Internship Project

This project was developed as part of an Artificial Intelligence internship.

````

## Your project is now complete

Your folder should contain:

```text
Project 3 - AI Book Recommendation System/
│
├── recommendation.py
├── books.csv
├── requirements.txt
├── .gitignore
└── README.md
````

### Next step: run the project

Open PowerShell inside the project folder and run:

```powershell
python recommendation.py
```

Then enter something like:

```text
Fantasy, Adventure, Mystery
```



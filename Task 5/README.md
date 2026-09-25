# AI Spam Email Classifier

## Project Overview

The AI Spam Email Classifier is a machine learning project that automatically classifies email messages as either **Spam** or **Not Spam**.

The system uses Natural Language Processing (NLP) techniques to convert email text into numerical features and then uses a machine learning algorithm to learn patterns associated with spam messages.

---

## Features

- Email text preprocessing
- Automatic text cleaning
- TF-IDF feature extraction
- Machine learning classification
- Spam and Not Spam prediction
- Model accuracy evaluation
- Classification report
- Confidence score for predictions
- Interactive custom email testing

---

## How It Works

The system follows these steps:

1. Loads the email dataset.
2. Cleans the email text.
3. Splits the dataset into training and testing data.
4. Converts text into numerical features using TF-IDF.
5. Trains a Multinomial Naive Bayes classifier.
6. Evaluates the model using test data.
7. Allows the user to enter a custom email.
8. Predicts whether the email is Spam or Not Spam.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF
- Multinomial Naive Bayes

---

## Dataset

The training data is stored in:

```text
emails.csv
````

The dataset contains two columns:

```text
label
text
```

Example:

```text
label,text
ham,"Please send me the project report."
spam,"Congratulations! You have won a free prize!"
```

Where:

* `ham` = Not Spam
* `spam` = Spam

---

## Project Structure

```text
Project 5 - AI Spam Email Classifier/
│
├── spam_classifier.py
├── emails.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the classifier:

```bash
python spam_classifier.py
```

The program will train the machine learning model and display its performance.

After training, you can enter your own email message.

Example:

```text
Email text: Congratulations! You have won a free cash prize. Click now!
```

Example result:

```text
Prediction: SPAM
Confidence: 94.25%
```

---

## Machine Learning Method

### TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts email text into numerical features that the machine learning model can understand.

### Multinomial Naive Bayes

Multinomial Naive Bayes is used to classify the processed email text into spam or not spam categories.

---

## Model Evaluation

The system evaluates the model using:

* Accuracy
* Precision
* Recall
* F1-score

The classification report is displayed after training.

---

## Author

Maheen Kanwal

---

## Internship Project

This project was developed as part of an Artificial Intelligence internship.

````

## Project 5 is now ready

Your folder should contain:

```text
Project 5 - AI Spam Email Classifier/
│
├── spam_classifier.py
├── emails.csv
├── requirements.txt
├── .gitignore
└── README.md
````

### Next: test it

From PowerShell inside the Project 5 folder:

```powershell
python -m pip install -r requirements.txt
```

Then:

```powershell
python spam_classifier.py
```

When it asks for an email, test it with:

```text
Congratulations! You have won a free cash prize. Click now to claim your reward!
```

Then test a normal message:

```text
Hi, please send me the project report when you have time.
```
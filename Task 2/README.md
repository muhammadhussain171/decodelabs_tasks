# Data Classification System

## Project Overview

The Data Classification System is a machine learning project that classifies iris flowers into different species based on their physical measurements.

The system uses four numerical features:

- Sepal length
- Sepal width
- Petal length
- Petal width

Based on these features, the trained model predicts one of three flower classes:

- Setosa
- Versicolor
- Virginica

## Features

- CSV dataset loading
- Dataset validation
- Missing-value handling
- Feature scaling
- Machine learning model training
- Train/test data splitting
- Accuracy evaluation
- Classification report
- Custom data prediction

## Machine Learning Algorithm

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm.

KNN classifies a new data point by comparing it with nearby examples in the training dataset.

Before classification, `StandardScaler` is used to scale the numerical features so that the measurements are on a comparable scale.

## How It Works

The system follows these steps:

1. Load the CSV dataset.
2. Validate the required columns.
3. Remove incomplete records.
4. Separate features and target classes.
5. Split the data into training and testing sets.
6. Scale the numerical features.
7. Train the KNN classifier.
8. Test the model on unseen data.
9. Calculate the classification accuracy.
10. Display a classification report.
11. Allow the user to enter custom measurements.
12. Predict the flower species.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Machine Learning
- K-Nearest Neighbors
- StandardScaler

## Dataset

The dataset is stored in:

```text
data.csv
````

It contains the following columns:

```text
sepal_length
sepal_width
petal_length
petal_width
species
```

## Project Structure

```text
Task 2/
│
├── data_classifier.py
├── data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Make sure Python 3.x is installed.

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Running the Project

Run:

```bash
python data_classifier.py
```

The program will train the classification model and display its performance.

After training, it will ask for four flower measurements.

Example:

```text
Sepal length: 5.1
Sepal width: 3.5
Petal length: 1.4
Petal width: 0.2
```

Example prediction:

```text
Predicted class: setosa
```

## Model Evaluation

The system evaluates the model using:

* Accuracy
* Precision
* Recall
* F1-score

A classification report is displayed after the model is tested.

## Example Workflow

```text
Loading dataset...
Dataset loaded successfully!

Total records: 60
Number of classes: 3

Training classification model...
Model trained successfully!

Accuracy: XX.XX%

Classification Report:
...

CUSTOM DATA CLASSIFICATION

Sepal length: 5.1
Sepal width: 3.5
Petal length: 1.4
Petal width: 0.2

Predicted class: setosa
```

## Limitations

The model is trained on a relatively small dataset. Its predictions may therefore not represent all possible flower varieties or measurements.

## Future Improvements

Possible improvements include:

* Using a larger dataset
* Comparing multiple classification algorithms
* Adding data visualization
* Adding a graphical user interface
* Saving the trained model
* Adding confusion matrix visualization

## Author

Maheen Kanwal

## Internship Project

This project was developed as part of an Artificial Intelligence internship.

````


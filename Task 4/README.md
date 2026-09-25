# AI Image Recognition System

## Project Overview

The AI Image Recognition System is a Python-based application that uses a pre-trained artificial intelligence model to recognize and classify multiple images automatically.

Instead of analyzing only one image, the system scans an `images` folder and analyzes all supported images available in that folder.

The AI model provides the top predictions along with confidence scores for each image.

---

## Features

- Uses a pre-trained AI image classification model
- Automatically analyzes multiple images
- Supports JPG, JPEG, PNG, and WEBP images
- Displays the best prediction
- Displays confidence percentage
- Provides confidence assessment
- Shows the top 5 predictions
- Generates a final project summary
- Automatically checks the images folder

---

## How It Works

1. The program loads a pre-trained Vision Transformer (ViT) model.
2. The program checks the `images` folder.
3. All supported images are detected automatically.
4. Each image is analyzed individually.
5. The AI model generates classification predictions.
6. The top 5 predictions are displayed.
7. A confidence score is shown for each prediction.
8. The program displays a final summary.

---

## Technologies Used

- Python
- Artificial Intelligence
- Computer Vision
- Hugging Face Transformers
- PyTorch
- Torchvision
- Pillow

---

## Project Structure

```text
Project 4 - AI Image Recognition/
│
├── recognition.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── images/
    ├── image1.jpg
    ├── image2.jpg
    └── image3.png
````

---

## Installation

Clone or download the project.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows PowerShell

```powershell
venv\Scripts\activate
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Use

Place your images inside the `images` folder.

Example:

```text
images/
├── dog.jpg
├── cat.jpg
├── car.png
└── building.jpg
```

Run the program:

```bash
python recognition.py
```

The system will automatically analyze all supported images.

---

## Supported Image Formats

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`

---

## Example Output

```text
======================================================================
                    AI IMAGE RECOGNITION SYSTEM
======================================================================

Loading pre-trained AI model...
Please wait...

Model loaded successfully!

Checking image folder...

Images available: 3

======================================================================
ANALYZING IMAGE
======================================================================

Image: dog.jpg
Size: 6000 x 4000

-----------------------------------------------------------------
BEST PREDICTION
-----------------------------------------------------------------

Prediction : golden retriever
Confidence : 85.42%
Assessment : Very High Confidence

TOP 5 PREDICTIONS
-----------------------------------------------------------------

1. golden retriever                         85.42%
2. Labrador retriever                       7.31%
3. cocker spaniel                           2.14%
4. Irish setter                             1.25%
5. German shepherd                          0.98%

======================================================================
PROJECT SUMMARY
======================================================================

Total images found: 3
Successfully analyzed: 3
Failed analyses: 0

AI Image Recognition System completed successfully!
```

---

## Author

Maheen Kanwal

---

## Internship Project

This project was developed as part of an Artificial Intelligence internship.

````

## Current Project 4 structure

```text
Project 4 - AI Image Recognition/
│
├── recognition.py
├── requirements.txt
├── .gitignore
├── README.md
└── images/
````

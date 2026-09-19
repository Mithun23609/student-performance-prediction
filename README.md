# Student Performance Prediction

A Machine Learning based Student Performance Prediction System built using Python and Flask.

## Project Overview

This project predicts a student's academic outcome based on 36 input features.

The prediction classes are:

- Dropout
- Enrolled
- Graduate

## Machine Learning Models

The project was evaluated using:

- Logistic Regression
- Random Forest
- XGBoost

### Logistic Regression Results

- Accuracy: 76.84%
- F1 Score: 75.77%

### Random Forest Results

- Accuracy: 76.50%
- F1 Score: 74.46%

### XGBoost Results

- Accuracy: 76.50%
- F1 Score: 75.31%

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Joblib
- HTML/CSS

## Features

The model uses 36 student-related features including:

- Admission grade
- Previous qualification
- Age at enrollment
- Scholarship status
- Tuition fee status
- First semester academic information
- Second semester academic information
- Economic indicators

## How to Run

```bash
pip install -r requirements.txt
python app.py

Then open:

http://127.0.0.1:5000

Project Structure
student-performance-prediction/
├── app.py
├── feature_names.pkl
├── student_prediction_model.pkl
├── requirements.txt
├── .gitignore
└── templates/
    ├── index.html
    └── result.html

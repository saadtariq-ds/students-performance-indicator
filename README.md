# 📚 Student Performance Indicator
## 📖 Project Overview

The Student Performance Indicator project aims to predict student academic performance based on various demographic and educational factors such as gender, parental education level, lunch type, and test preparation course.

The project applies multiple regression algorithms to analyze how different features influence student performance and determine the most accurate predictive model.

This project demonstrates an end-to-end machine learning workflow, including data preprocessing, feature engineering, model training, evaluation, and performance comparison.

## 📊 Dataset Description

The dataset contains information about students and their exam scores.
| Feature | Description |
|---------|------|
| gender | Student gender |
| race_ethnicity | Student ethnicity group |
| parental_level_of_education | Parent education level |
| lunch | Standard or free/reduced lunch |
| test_preparation_course | Completed test preparation or not |
| reading_score | Reading exam score |
| writing_score | Writing exam score |
| math_score | Student math exam score |

## ⚙️ Project Workflow

1️⃣ Data Collection

2️⃣ Data Preprocessing

3️⃣ Exploratory Data Analysis (EDA)

4️⃣ Feature Engineering

5️⃣ Model Training

6️⃣ Model Evaluation

7️⃣ Model Comparison

## 🤖 Machine Learning Models Used

1️⃣ Linear Regression

2️⃣ Decision Tree

3️⃣ Random Forest

4️⃣ Ada Boost

5️⃣ Gradient Boosting

6️⃣ XgBoost

7️⃣ Catboost

# ⚙️ Setup & Run Locally
## 1️⃣ Clone
```bash
git clone https://github.com/saadtariq-ds/students-performance-indicator.git
cd students-performance-indicator
```

## 2️⃣ Create virtual environment (recommended)
```bash
python -m venv ven
source venv/bin/activate   # Windows: venv\Scripts\activate
```

## 3️⃣ Install requirements
```bash
pip install -r requirements.txt
```

## 4️⃣ Run Training Pipeline
```bash
python src\pipeline\training_pipeline.py
```

## 5️⃣ Run Flask App
```bash
python app.py
```

# 💻 Laptop Price Prediction System

An end-to-end Machine Learning web application that predicts the price of a laptop based on Brand, RAM size, and Storage capacity.
The project integrates ML model training, a Flask backend API, and a modern frontend UI built with HTML, CSS, and JavaScript.

## 📌 Project Overview

Laptop prices vary based on specifications such as brand, memory, and storage.
This project uses Machine Learning (Regression) to predict laptop prices and provides a user-friendly web interface for real-time predictions.

## 🚀 Features

🔍 Predict laptop price using:

Brand

RAM Size (GB)

Storage Capacity (GB)

🤖 Trained Machine Learning regression model

🌐 Flask REST API for predictions

🎨 Clean and responsive frontend UI

🔄 Real-time prediction without page reload

📦 Model and scaler persistence using Pickle

## 🧠 Machine Learning Details

Type: Supervised Learning

Problem: Regression

Algorithm Used: Linear Regression

Evaluation Metric: R² Score

Accuracy Achieved: ~0.99 (on test data)

## 🛠️ Tech Stack
#### 🔹 Backend & ML

Python

Pandas

NumPy

Scikit-learn

Flask

Flask-CORS

Pickle

#### 🔹 Frontend

HTML

CSS

JavaScript (Fetch API)

#### 🔹 Tools

VS Code

Jupyter Notebook

GitHub


## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
git clone https://github.com/your-username/laptop-price-prediction.git
cd laptop-price-prediction

### 2️⃣ Create & Activate Virtual Environment
python -m venv .venv


Windows

.venv\Scripts\activate


Linux / Mac

source .venv/bin/activate

### 3️⃣ Install Dependencies
pip install flask flask-cors numpy pandas scikit-learn

### 🧪 Model Training (Optional)

Model training is done in:

notebook/data_analysis.ipynb


Steps include:

Data loading

Feature selection

One-hot encoding (Brand)

Feature scaling

Model training

Model saving (.pkl)

## ▶️ Running the Application
🔹 Start Backend (Flask API)
cd backend
python app.py

# 💳 AI Payment Risk Prediction System

This project is an end-to-end Machine Learning system designed to predict payment default risk and detect anomalies in financial transactions.

# 🚀 Features

- Data generation simulating real-world financial behavior
- Data cleaning and preprocessing pipeline
- Feature engineering based on customer behavior
- Machine Learning models for prediction
- Anomaly detection using Isolation Forest
- API for real-time predictions
- Dashboard integration (Power BI)

## 🧠 Problem

Companies often struggle to identify customers who are likely to delay or default on payments. This project aims to solve this problem using data-driven approaches.

## 🏗️ Architecture

data → processing → features → model → API → dashboard

## 📊 Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- PyTorch (future step)
- FastAPI
- Power BI

# 📁 Project Structure

src/
data/
models/
api/

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/data/generate_data.py
```

## 🎯 Goals

- Predict if a customer will pay on time
- Detect suspicious or anomalous transactions
- Provide insights for decision-making

## 📌 Future Improvements

- Deep Learning models (PyTorch)
- Real-time data pipeline
- Model deployment on cloud
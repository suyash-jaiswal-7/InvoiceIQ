# 📦 InvoiceIQ — AI-Powered Invoice Intelligence Platform

**InvoiceIQ** is a machine learning-powered invoice intelligence platform designed to streamline vendor invoice operations through freight cost prediction and invoice risk flagging.

It combines regression and classification models to help finance teams forecast freight expenses and identify invoices that may require manual approval.

<p align="center">
  <a href="https://invoice-iq-ml.streamlit.app/"><strong>🚀 Live Demo</strong></a>
</p>

## 🌟 Overview

InvoiceIQ provides two core prediction modules:

- **Freight Cost Prediction:** Estimates freight costs using invoice dollar value.
- **Invoice Manual Approval Flagging:** Predicts whether an invoice should be flagged for manual review using invoice and purchase-related information.

The platform provides an interactive Streamlit interface for submitting invoice details and viewing model predictions.

## ✨ Features

### 1. Freight Cost Prediction
- Machine learning-based regression.
- Uses invoice dollar value as the input feature.
- Estimates expected freight costs.
- Supports budgeting and vendor cost forecasting.

### 2. Invoice Manual Approval Flagging
- Machine learning-based classification.
- Evaluates invoice and purchase information.
- Uses five input features:
  - Invoice Quantity
  - Invoice Dollars
  - Freight Cost
  - Total Item Quantity
  - Total Item Dollars
- Identifies invoices that may require manual review.

### 3. Interactive Dashboard
- Streamlit-powered web interface.
- Separate modules for regression and classification.
- Interactive input forms and prediction results.
- Business-oriented dashboard design.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Frontend | Streamlit |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## 🧠 Machine Learning Workflow

The project follows a typical machine learning pipeline:

1. Data loading and exploration
2. Data preprocessing and feature selection
3. Feature scaling where required
4. Model training and hyperparameter tuning
5. Model evaluation
6. Model serialization using Joblib
7. Prediction through separate inference modules
8. Integration with the Streamlit application

### Models

| Module | ML Task | Model |
|---|---|---|
| Freight Cost Prediction | Regression | Best-performing model selected during training |
| Invoice Flagging | Classification | Random Forest Classifier |

## 📸 Application Screenshots

### Homepage
![InvoiceIQ Homepage](docs/images/homepage.png)

### Freight Cost Prediction
![Freight Cost Prediction](docs/images/freight-prediction.png)

### Invoice Manual Approval Flagging
![Invoice Manual Approval Flagging](docs/images/invoice-flagging.png)

## 📁 Project Structure

```text
InvoiceIQ/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── freight_cost_prediction/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── train.py
│
├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
│       ├── predict_flag_invoice.pkl
│       └── scaler.pkl
│
├── inferencing/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── models/
│   ├── predict_freight_model.pkl
│   └── scaler.pkl
│
└── notebooks/
    ├── Invoice Flagging.ipynb
    └── Predicting Freight Cost.ipynb
```

## ⚙️ Installation and Local Setup

### Prerequisites
- Python 3.11
- Git

### 1. Clone the repository

```bash
git clone https://github.com/suyash-jaiswal-7/InvoiceIQ.git
cd InvoiceIQ
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🚀 Deployment

InvoiceIQ is deployed using **Streamlit Community Cloud**.

**Live Application:** https://invoice-iq-ml.streamlit.app/

## 🔮 Future Improvements

- Improve model performance through additional feature engineering.
- Expand invoice anomaly detection capabilities.
- Introduce explainable AI for prediction insights.
- Add invoice document upload and automated data extraction.
- Develop historical prediction analytics and reporting.

## 👨‍💻 Author

**Suyash Jaiswal**

B.Tech — Computer Science and Engineering (Data Science)

- GitHub: [suyash-jaiswal-7](https://github.com/suyash-jaiswal-7)
- Project Repository: [InvoiceIQ](https://github.com/suyash-jaiswal-7/InvoiceIQ)
- Live Demo: [InvoiceIQ on Streamlit](https://invoice-iq-ml.streamlit.app/)

---

<p align="center">
  <strong>InvoiceIQ — Making Invoice Operations Smarter with Machine Learning.</strong>
</p>

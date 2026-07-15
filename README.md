# 💼 Employee Salary Prediction

> **An end-to-end machine learning project that predicts employee annual salaries using Linear Regression. The project covers exploratory data analysis (EDA), data preprocessing, model development, evaluation, and deployment with Streamlit.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📌 Business Problem

Organisations often need to estimate employee salaries based on workforce characteristics such as experience and performance. Accurate salary prediction can support budgeting, workforce planning, compensation benchmarking, and HR decision-making.

This project builds a machine learning model that predicts an employee's **annual salary** using historical employee data.

---

# 🎯 Objectives

- Explore and understand employee salary data
- Identify factors that influence salaries
- Build a predictive machine learning model
- Evaluate model performance
- Deploy the model using Streamlit

---

# 📊 Dataset

The dataset contains **689 employee records** with **15 attributes** collected from organisations across Egypt, Saudi Arabia, UAE, Syria, and Lebanon.

### Dataset Summary

| Metric | Value |
|---------|------:|
| Records | 689 |
| Features | 15 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

### Features

- Gender
- Start Date
- Years at Company
- Department
- Country
- Branch Centre
- Monthly Salary
- Job Rate
- Sick Leaves
- Unpaid Leaves
- Overtime Hours

**Target Variable**

- Annual Salary

---

# 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Data Analysis |
| Pandas | Data Cleaning |
| Matplotlib | Visualisation |
| Scikit-Learn | Machine Learning |
| Joblib | Model Serialization |
| Streamlit | Model Deployment |

---

# 🔄 Machine Learning Workflow

```text
Employee Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Selection
        │
        ▼
Train/Test Split
        │
        ▼
Linear Regression
        │
        ▼
Model Evaluation
        │
        ▼
Streamlit Prediction App
```

---

# 📈 Exploratory Data Analysis

Key findings from the dataset include:

- Male employees account for **65%** of the workforce.
- Most employees have performance ratings between **3 and 5**.
- Overtime hours are highly variable, ranging from **0 to 198 hours**.
- Annual salaries range from **$8,436** to **$41,400**.
- Salary distributions differ across departments and branch centres.

---

# 🤖 Model Development

## Algorithm

- Linear Regression

## Selected Features

- Years at Company
- Job Rate

## Train/Test Split

- Training: **80%**
- Testing: **20%**

---

# 📊 Model Performance

| Metric | Result |
|---------|-------:|
| Mean Absolute Error (MAE) | ~$7,703 |

### Interpretation

The model successfully captures the relationship between employee experience, performance, and salary. While Linear Regression provides a solid baseline model, prediction accuracy can be improved by incorporating additional employee attributes and experimenting with more advanced algorithms.

---

# 💡 Business Insights

- Employee experience has a measurable impact on salary.
- Higher-performing employees generally earn higher salaries.
- Salary differences exist between departments and branch locations.
- Additional variables such as overtime, department, and country are likely to improve prediction accuracy.

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/AngeloGeno/Machine-learning-Salary-Prediction.git

cd Machine-learning-Salary-Prediction
```

## Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn streamlit joblib openpyxl
```

## Run the notebook

Open:

```
Analysis_Modeling.ipynb
```

to reproduce the exploratory analysis and model training.

## Launch the application

```bash
streamlit run app.py
```
# 📷 Application Preview

<p align="center">
  <img src="/App_Screenshot_1.png" alt="Employee Salary Prediction Streamlit App" width="900"/>
</p>
---

# 📂 Repository Structure

```text
Machine-learning-Salary-Prediction
│
├── Analysis_Modeling.ipynb
├── Employees.xlsx
├── app.py
├── linearmodel.pkl
├── screenshots
│   └── app.png
└── README.md
```

---

# 📷 Application Preview

> Add screenshots of your Streamlit application here.

Example:

App_Screenshot_1.png
---

# 📚 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualisation
- Feature Selection
- Machine Learning
- Linear Regression
- Model Evaluation
- Streamlit Deployment
- Python
- Scikit-Learn

---

# 🔮 Future Improvements

- Incorporate additional predictive features such as department, country, and overtime hours.
- Compare multiple regression algorithms (Random Forest, Gradient Boosting, XGBoost).
- Perform hyperparameter tuning.
- Use k-fold cross-validation for more robust evaluation.
- Deploy the application publicly using Streamlit Community Cloud.

---

# 👤 Author

**Angelo Geno Nkomo**

- 💼 Junior Data Analyst & Software Developer
- GitHub: https://github.com/AngeloGeno
- LinkedIn: *(Add your LinkedIn profile)*

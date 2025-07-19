# 🌾 Soil Quality Prediction Using Random Forest & Elephant Herding Optimization 🐘

A machine learning–powered web application for predicting **Soil Quality Index (SQI)** based on chemical and environmental soil properties. This project integrates **Random Forest Regressor** for prediction and **Elephant Herding Optimization (EHO)** for hyperparameter tuning. A simple **Flask-based web interface** allows users to interactively input soil parameters and get real-time predictions.

---

## 🧪 Objective

- Predict the **Soil Quality Index** using features such as:
  - Nitrogen, Phosphorus, Potassium
  - Temperature, Humidity, pH, Rainfall
- Optimize model accuracy using **Elephant Herding Optimization**
- Deploy the solution via a user-friendly **Flask web application**

---

## 📚 Dataset

- **Source**: Crop recommendation dataset adapted for soil quality analysis
- **Features**:
  - `Nitrogen`, `Phosphorus`, `Potassium`
  - `Temperature`, `Humidity`, `pH_Value`, `Rainfall`
- **Target**:
  - `Soil Quality Index (SQI)` — a derived value

> 📌 *The dataset was cleaned and restructured for regression modeling.*

---

## 🤖 Machine Learning Model

- **Model Used**: `RandomForestRegressor` from `scikit-learn`
- **Why Random Forest?**
  - Handles nonlinear relationships
  - Works well with tabular, heterogeneous data
  - Provides good performance with minimal tuning

---

## 🐘 Elephant Herding Optimization (EHO)

EHO is a **nature-inspired metaheuristic algorithm** based on elephant clan behavior. We implemented a **custom version** without external libraries to optimize two hyperparameters:

- `n_estimators` (number of trees)
- `max_depth` (tree depth)

### How It Works:
- Each **elephant = a candidate solution**
- The **clan moves** toward the **best-performing elephant**
- Optimization is driven by minimizing **Mean Absolute Error (MAE)**
- Optionally: worst elephants can be **randomly reinitialized**

---

## 🖥 Flask Web Application

A minimal web interface using **Flask + HTML** to allow users to:
- Enter soil parameters through a form
- Submit and receive the predicted **Soil Quality Index**
- See results in real time

### Demo Preview:
![Alt Text](/website.png)

---

## 📁 Project Structure

Soil-Quality-EHO-Project/
│
├── app.py                      # Flask backend logic
├── rf_model.pkl                # Trained Random Forest model
├── Dataset_Exploration.ipynb  # Main notebook with ML + EHO logic
├── Untitled.ipynb             # Unused - consider deleting or merging
├── Crop_Recommendation.csv    # Dataset used for training
├── README.md                  # Full project overview and documentation
├── website.png                # Screenshot for README UI preview
│
├── templates/                 # HTML templates folder
│   └── index.html             # Main UI form for user input
│
├── .ipynb_checkpoints/        # Auto-created by Jupyter (can be gitignored)
│
└── .gitignore                 # To ignore unwanted files during Git push


## 📈 Results

| Metric       | Value      |
|--------------|------------|
| MAE (Before EHO) | 0.0121     |
| MAE (After EHO)  | **0.0119** |
| Best Parameters | `n_estimators = 114`, `max_depth = 22` |

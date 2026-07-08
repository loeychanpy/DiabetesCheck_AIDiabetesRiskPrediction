# DiabetesCheck — AI Diabetes Risk Prediction

A web-based diabetes risk prediction system built with Flask and a C4.5 Decision Tree model trained on the BRFSS 2015 health survey dataset.

## Features

- Predicts diabetes risk from 5 health indicators
- BMI is calculated automatically from height and weight inputs
- Displays prediction confidence (probability score)
- Clean, responsive UI built with Bootstrap

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| ML Model | Scikit-Learn `DecisionTreeClassifier` (C4.5 / entropy) |
| Data | Pandas |
| Server | Waitress (production) |

## Model Details

- **Algorithm**: C4.5 Decision Tree (`criterion='entropy'`, `max_depth` tuned via 5-Fold CV)
- **Dataset**: BRFSS 2015 — 253,680 respondents, binary classification (No Diabetes vs Diabetes)
- **Class imbalance handling**: Undersampling on training set only (4.8:1 majority ratio)
- **Features**: `HighBP`, `HighChol`, `BMI`, `GenHlth`, `Age`

### Performance (on unbalanced test set)

| Metric | Score |
|---|---|
| Accuracy | 68.12% |
| Balanced Accuracy | 72.13% |
| ROC-AUC | 0.798 |

> Balanced Accuracy and ROC-AUC are the primary metrics used due to class imbalance.

## Project Structure

```
AIDiabetes/
├── app.py                          # Flask app & prediction routes
├── requirements.txt
├── render.yaml                     # Render deployment config
├── model/
│   ├── model_c45_diabetes.pkl      # Trained C4.5 model
│   └── diabetes_012_health_indicators_BRFSS2015.csv
└── templates/
    ├── base.html
    ├── index.html                  # Prediction form & result
    ├── about.html                  # Project info
    └── profile.html                # Team profiles
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/loeychanpy/AIDiabetes.git
cd AIDiabetes
pip install -r requirements.txt
```

### Run locally

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Prediction form |
| `/predict` | POST | Run prediction and return result |
| `/about` | GET | Project and model information |
| `/profile` | GET | Team profiles |

## Team — Kelompok 10

| Name | Role |
|---|---|
| Zakharia | Data Scientist — model training, dataset cleaning, evaluation |
| Janisha Jaya | Project Manager & Developer — Flask, UI, model integration |
| Erivol | Documentation — technical report (Bab I–V) |

*Final project for Machine Learning — UAS Semester Genap*

---

> **Disclaimer**: Predictions are indicative only and based on survey data, not a medical diagnosis. Consult a doctor for clinical evaluation.
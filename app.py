import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# ============================================================
# Model C4.5 (Decision Tree) - dataset BRFSS2015
# ============================================================
with open("model/model_c45_diabetes.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Urutan fitur HARUS sama persis dengan saat training
FEATURES = ['HighBP', 'HighChol', 'BMI', 'GenHlth', 'Age']
LABEL = ['Tidak Diabetes', 'Positif Diabetes']  # index 0 dan 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # BMI dihitung otomatis dari tinggi & berat badan
        height = float(request.form['height'])   # cm
        weight = float(request.form['weight'])    # kg
        bmi = round(weight / ((height / 100) ** 2), 1)

        input_data = {
            'HighBP':   int(request.form['HighBP']),
            'HighChol': int(request.form['HighChol']),
            'BMI':      bmi,
            'GenHlth':  int(request.form['GenHlth']),
            'Age':      int(request.form['Age']),
        }

        new_data = pd.DataFrame([input_data], columns=FEATURES)

        prediction = int(model.predict(new_data)[0])
        proba = model.predict_proba(new_data)[0][prediction] * 100
        result = LABEL[prediction]

        input_data['height'] = height
        input_data['weight'] = weight

        return render_template('index.html',
                               result=result,
                               proba=round(proba, 1),
                               is_positive=(prediction == 1),
                               inputs=input_data)

    except (ValueError, KeyError) as e:
        return render_template('index.html', error=f"Input tidak valid: {e}")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    from waitress import  serve
    serve(app , host='0.0.0.0' , port=5000)
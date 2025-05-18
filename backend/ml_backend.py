import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "machine_learning_model", "model.pkl")

print("Lade Modell von:", model_path)

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Modell nicht gefunden: {model_path}")

model = joblib.load(model_path)

FEATURES = [
    "school", "sex", "age", "address", "famsize", "Pstatus",
    "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
    "traveltime", "studytime", "failures",
    "schoolsup", "famsup", "paid", "activities", "nursery", "higher",
    "internet", "romantic", "famrel", "freetime", "goout",
    "Dalc", "Walc", "health", "absences"
]

def preprocess_form(form):
    data = {feature: form.get(feature) for feature in FEATURES}

    numeric_fields = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures",
                      "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences"]
    for field in numeric_fields:
        data[field] = int(data[field])

    df = pd.DataFrame([data])
    return df

def predict_grade(input_df):
    prediction = model.predict(input_df)[0]
    return round(prediction, 2)

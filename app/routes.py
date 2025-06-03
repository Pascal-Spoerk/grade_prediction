from app import app
from flask import render_template, request
from backend.ml_backend import preprocess_form, predict_grade

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_df = preprocess_form(request.form)
        prediction = predict_grade(input_df)
    return render_template("index.html", prediction=prediction)
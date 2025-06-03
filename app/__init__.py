from flask import Flask, render_template, request
from backend.ml_backend import preprocess_form, predict_grade

app = Flask(__name__, template_folder="../frontend/templates")

from app import routes
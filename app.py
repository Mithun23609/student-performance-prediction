from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("student_prediction_model.pkl")
feature_names = joblib.load("feature_names.pkl")


@app.route("/")
def home():
    return render_template("index.html", features=feature_names)


@app.route("/predict", methods=["POST"])
def predict():

    input_data = {}

    for feature in feature_names:
        value = request.form.get(feature)

        try:
            input_data[feature] = float(value)
        except (ValueError, TypeError):
            return "Invalid input. Please enter numeric values."

    input_df = pd.DataFrame(
        [input_data],
        columns=feature_names
    )

    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities) * 100

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=round(confidence, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
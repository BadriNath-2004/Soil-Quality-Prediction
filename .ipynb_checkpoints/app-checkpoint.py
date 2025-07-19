from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            # Match input names with dataset column names
            nitrogen = float(request.form["Nitrogen"])
            phosphorus = float(request.form["Phosphorus"])
            potassium = float(request.form["Potassium"])
            temperature = float(request.form["Temperature"])
            humidity = float(request.form["Humidity"])
            ph_value = float(request.form["pH_Value"])
            rainfall = float(request.form["Rainfall"])

            # Create input array for model
            features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]])

            # Predict Soil Quality Index
            prediction = model.predict(features)[0]
        except:
            prediction = "Invalid input!"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

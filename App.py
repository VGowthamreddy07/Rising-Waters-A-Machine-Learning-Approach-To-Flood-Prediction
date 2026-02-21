from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model
model = pickle.load(open("flood_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rainfall = float(request.form['rainfall'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    water_level = float(request.form['water_level'])

    features = np.array([[rainfall, temperature, humidity, water_level]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "⚠ Flood Risk Detected!"
    else:
        result = "✅ No Flood Risk"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

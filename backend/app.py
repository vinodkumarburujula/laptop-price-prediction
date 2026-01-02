from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

model = pickle.load(open("../model/laptop_model.pkl", "rb"))
scaler = pickle.load(open("../model/scaler.pkl", "rb"))

@app.route("/")
def home():
    return "Laptop Price Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    ram = data["RAM_Size"]
    storage = data["Storage_Capacity"]
    brand = data["Brand"]

    # One-hot encoding (MUST match X.columns exactly)
    brand_asus = 1 if brand == "Asus" else 0
    brand_dell = 1 if brand == "Dell" else 0
    brand_hp = 1 if brand == "HP" else 0
    brand_lenovo = 1 if brand == "Lenovo" else 0

    # EXACT feature order
    features = [
        ram,
        storage,
        brand_asus,
        brand_dell,
        brand_hp,
        brand_lenovo
    ]

    features_array = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features_array)
    prediction = model.predict(scaled_features)

    return jsonify({
        "predicted_price": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

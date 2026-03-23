from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# modelo simple
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 55, 65, 70, 80])

modelo = LinearRegression()
modelo.fit(X, y)

@app.route("/")
def home():
    return {"mensaje": "API IA funcionando 🚀"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    horas = data["horas"]
    pred = modelo.predict([[horas]])
    return jsonify({"resultado": float(pred[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, jsonify
from predict import predict_irrigation
import numpy as np

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    # Generate data and get prediction
    soil_moisture, temperature, humidity, prediction = predict_irrigation()

    # Respond with values and prediction
    return jsonify({
        "Soil_Moisture": round(soil_moisture, 2),
        "Temperature": round(temperature, 2),
        "Humidity": round(humidity, 2),
        "Irrigation_Required": int(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
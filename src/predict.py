import joblib
import numpy as np

def generate_random_values():
    soil_moisture = np.random.uniform(314.51, 984.83)
    temperature = np.random.uniform(18.00, 38.99)
    humidity = np.random.uniform(38.00, 81.27)
    random_data = np.array([[soil_moisture, temperature, humidity]])
    
    # Load scaler and scale data
    scaler = joblib.load("../models/scaler.pkl")
    scaled_data = scaler.transform(random_data)
    return soil_moisture, temperature, humidity, scaled_data

def predict_irrigation():
    # Generate random data
    soil_moisture, temperature, humidity, scaled_data = generate_random_values()
    print("Input Data:", scaled_data)
    
    # Load trained model
    knn = joblib.load("../models/knn_model.pkl")
    prediction = knn.predict(scaled_data)
    return soil_moisture, temperature, humidity, prediction[0]

if __name__ == "__main__":
    soil_moisture, temperature, humidity, prediction = predict_irrigation()
    print("Irrigation Required" if prediction else "No Irrigation")
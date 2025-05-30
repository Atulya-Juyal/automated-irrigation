import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Save the scaler for prediction use
    joblib.dump(scaler, "../models/scaler.pkl")
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data("../data/sensor_data.csv")
    print("Preprocessing Complete!")
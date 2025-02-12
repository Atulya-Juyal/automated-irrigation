import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from preprocess_data import preprocess_data

def train_model():
    X_train, X_test, y_train, y_test = preprocess_data("../data/sensor_data.csv")
    
    # Train KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = knn.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    # Save the trained model
    joblib.dump(knn, "../models/knn_model.pkl")
    print("Model Training Complete!")

if __name__ == "__main__":
    train_model()
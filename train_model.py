import os

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


DATA_FILE = "crop_data.csv"
MODEL_DIR = "models"
MODEL_FILE = os.path.join(MODEL_DIR, "crop_model.pkl")


FEATURES = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
]


def train_model():
    print("Loading dataset...")

    data = pd.read_csv(DATA_FILE)

    print(f"Dataset size: {len(data)} rows")
    print(f"Crops: {sorted(data['label'].unique())}")

    X = data[FEATURES]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("\nTraining Random Forest...")

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(model, MODEL_FILE)

    print(f"\nModel saved to: {MODEL_FILE}")


if __name__ == "__main__":
    train_model()
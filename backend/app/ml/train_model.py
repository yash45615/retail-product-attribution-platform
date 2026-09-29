from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report
)


BASE_DIR = Path(
    __file__
).resolve().parents[3]

DATA_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "clean_products.csv"
)

MODEL_FILE = (
    Path(__file__).resolve().parent
    / "product_classifier.joblib"
)


def train_model():

    df = pd.read_csv(
        DATA_FILE
    )

    df["text"] = (
        df["title"].fillna("")
        + " "
        + df["description"].fillna("")
        + " "
        + df["brand"].fillna("")
    )

    X = df["text"]
    y = df["category"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2)
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"Accuracy: {accuracy:.4f}"
    )

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    joblib.dump(
        model,
        MODEL_FILE
    )

    print(
        f"Model saved to {MODEL_FILE}"
    )


if __name__ == "__main__":
    train_model()
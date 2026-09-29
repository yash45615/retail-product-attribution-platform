from pathlib import Path

import joblib


MODEL_PATH = (
    Path(__file__).resolve().parent
    / "product_classifier.joblib"
)


class ProductPredictor:

    def __init__(self):

        if not MODEL_PATH.exists():

            raise FileNotFoundError(
                "ML model not found. "
                "Run: python -m app.ml.train_model"
            )

        self.model = joblib.load(
            MODEL_PATH
        )

    def predict(
        self,
        text: str
    ):

        category = self.model.predict(
            [text]
        )[0]

        probabilities = (
            self.model.predict_proba(
                [text]
            )[0]
        )

        confidence = float(
            probabilities.max()
        )

        return {
            "category": category,
            "confidence": confidence
        }
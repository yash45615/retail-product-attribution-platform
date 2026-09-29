from app.ml.predictor import (
    ProductPredictor
)

from app.services.regex_extractor import (
    extract_attributes
)

from app.services.product_type import (
    extract_product_type
)


class HybridAttributionEngine:

    def __init__(
        self,
        review_threshold: float = 0.80
    ):

        self.predictor = ProductPredictor()

        self.review_threshold = (
            review_threshold
        )

    def attribute(
        self,
        title: str,
        description: str = ""
    ):

        combined_text = (
            f"{title} {description}"
        )

        attributes = extract_attributes(
            title,
            description
        )

        product_type = extract_product_type(
            combined_text
        )

        prediction = self.predictor.predict(
            combined_text
        )

        confidence = prediction[
            "confidence"
        ]

        review_required = (
            confidence
            < self.review_threshold
        )

        return {
            "product_type": product_type,
            "attributes": attributes,
            "predicted_category":
                prediction["category"],
            "confidence": confidence,
            "review_required":
                review_required
        }
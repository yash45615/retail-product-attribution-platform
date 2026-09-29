import pandas as pd

from app.attribution.hybrid_engine import HybridAttributionEngine


class BatchAttributionService:

    def __init__(self):
        self.engine = HybridAttributionEngine()

    def process_dataframe(self, df: pd.DataFrame):

        results = []

        for _, row in df.iterrows():

            product_id = str(row.get("product_id", ""))

            title = str(row.get("title", ""))

            description = str(row.get("description", ""))

            brand = str(row.get("brand", ""))

            attribution = self.engine.attribute(
                title=title,
                description=description
            )

            results.append({
                "product_id": product_id,
                "title": title,
                "brand": brand,
                "product_type": attribution["product_type"],
                "predicted_category": attribution["predicted_category"],
                "confidence": attribution["confidence"],
                "review_required": attribution["review_required"],
                "status": (
                    "HUMAN_REVIEW"
                    if attribution["review_required"]
                    else "AUTO_APPROVED"
                )
            })

        return results
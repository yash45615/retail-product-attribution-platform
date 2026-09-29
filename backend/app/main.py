from fastapi import FastAPI
import pandas as pd
from pathlib import Path

from app.services.batch_attribution import BatchAttributionService
from app.attribution.hybrid_engine import (
    HybridAttributionEngine
)
batch_service = BatchAttributionService()
from app.services.review_service import (
    ReviewService
)

from app.schemas.product import (
    ProductRequest,
    ReviewDecision
)


app = FastAPI(
    title="Retail Product Attribution Intelligence Platform",
    description=(
        "ML-assisted retail product "
        "attribution platform"
    ),
    version="1.0.0"
)


engine = HybridAttributionEngine()

review_service = ReviewService()

review_queue = []


@app.get("/")
def root():

    return {
        "application":
            "Retail Product Attribution Intelligence Platform",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/api/attribute")
def attribute_product(
    product: ProductRequest
):

    result = engine.attribute(
        product.title,
        product.description
    )

    return {
        "product_id": product.product_id,
        **result
    }


@app.post("/api/reviews")
def create_review(
    product: ProductRequest
):

    attribution = engine.attribute(
        product.title,
        product.description
    )

    review = review_service.create_review(
        product.product_id,
        product.title,
        attribution
    )

    review_queue.append(review)

    return review


@app.get("/api/reviews")
def get_reviews():

    return {
        "count": len(review_queue),
        "items": review_queue
    }


@app.post("/api/reviews/decision")
def review_decision(
    decision: ReviewDecision
):

    for review in review_queue:

        if (
            review["product_id"]
            == decision.product_id
        ):

            return review_service.approve(
                review,
                decision.reviewer,
                decision.corrected_category,
                decision.corrected_subcategory
            )

    return {
        "error":
            "Review item not found"
    }


@app.get("/api/analytics")
def analytics():

    total = len(review_queue)

    pending = sum(
        1
        for review in review_queue
        if review["status"] == "PENDING"
    )

    auto_approved = sum(
        1
        for review in review_queue
        if review["status"]
        == "AUTO_APPROVED"
    )

    manually_approved = sum(
        1
        for review in review_queue
        if review["status"]
        == "APPROVED"
    )

    return {
        "total": total,
        "pending": pending,
        "auto_approved": auto_approved,
        "manually_approved":
            manually_approved
    }
@app.get("/api/attribute/batch")
def attribute_all_products():

    root_dir = Path(__file__).resolve().parents[2]

    csv_path = root_dir / "data" / "raw" / "products.csv"

    if not csv_path.exists():
        return {
            "error": "products.csv not found",
            "path": str(csv_path)
        }

    df = pd.read_csv(csv_path)

    results = batch_service.process_dataframe(df)

    # Clear old batch review records
    review_queue.clear()

    # Create review records for every product
    for result in results:

        review = review_service.create_review(
            result["product_id"],
            result["title"],
            {
                "product_type": result["product_type"],
                "predicted_category": result["predicted_category"],
                "confidence": result["confidence"],
                "review_required": result["review_required"],
                "attributes": {}
            }
        )

        review_queue.append(review)

    return {
        "total_products": len(results),
        "results": results,
        "review_queue_count": len(review_queue)
    }
from app.services.review_service import (
    ReviewService
)


def test_review_approval():

    service = ReviewService()

    review = {
        "product_id": "P001",
        "title": "Test Product",
        "prediction": {},
        "status": "PENDING",
        "reviewer": None,
        "corrected_category": None,
        "corrected_subcategory": None
    }

    result = service.approve(
        review,
        "Reviewer 1",
        "Footwear",
        "Running"
    )

    assert result["status"] == "APPROVED"

    assert (
        result["corrected_category"]
        == "Footwear"
    )
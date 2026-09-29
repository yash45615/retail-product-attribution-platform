class ReviewService:

    def create_review(
        self,
        product_id: str,
        title: str,
        attribution: dict
    ):

        status = (
            "PENDING"
            if attribution["review_required"]
            else "AUTO_APPROVED"
        )

        return {
            "product_id": product_id,
            "title": title,
            "prediction": attribution,
            "status": status,
            "reviewer": None,
            "corrected_category": None,
            "corrected_subcategory": None
        }

    def approve(
        self,
        review: dict,
        reviewer: str,
        corrected_category: str,
        corrected_subcategory: str
    ):

        review["status"] = "APPROVED"

        review["reviewer"] = reviewer

        review[
            "corrected_category"
        ] = corrected_category

        review[
            "corrected_subcategory"
        ] = corrected_subcategory

        return review
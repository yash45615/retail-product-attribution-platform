from pydantic import BaseModel


class ProductRequest(BaseModel):

    product_id: str

    title: str

    description: str = ""


class ReviewDecision(BaseModel):

    product_id: str

    reviewer: str

    corrected_category: str

    corrected_subcategory: str
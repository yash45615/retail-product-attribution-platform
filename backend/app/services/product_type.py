import re


PRODUCT_TYPES = {
    "running shoes": "Running Shoes",
    "sneakers": "Sneakers",
    "shoes": "Shoes",
    "jeans": "Jeans",
    "t-shirt": "T-Shirts",
    "t shirts": "T-Shirts",
    "shirt": "Shirts",
    "leggings": "Leggings",
    "television": "Television",
    "tv": "Television",
    "smartphone": "Smartphone",
    "phone": "Smartphone",
    "laptop": "Laptop",
    "headphones": "Headphones"
}


def extract_product_type(
    text: str
):

    text = text.lower()

    matches = []

    for keyword, product_type in PRODUCT_TYPES.items():

        if re.search(
            rf"\b{re.escape(keyword)}\b",
            text
        ):
            matches.append(
                (
                    len(keyword),
                    product_type
                )
            )

    if not matches:
        return "Other"

    matches.sort(
        reverse=True
    )

    return matches[0][1]
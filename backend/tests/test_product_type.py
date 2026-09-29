from app.services.product_type import (
    extract_product_type
)


def test_running_shoes():

    result = extract_product_type(
        "Nike Men's Running Shoes"
    )

    assert result == "Running Shoes"
from app.services.regex_extractor import (
    extract_attributes
)


def test_attribute_extraction():

    result = extract_attributes(
        "Nike Men's Running Shoes Black Size 10"
    )

    assert result["color"] == "Black"
    assert result["gender"] == "Men"
    assert result["size"] == "10"
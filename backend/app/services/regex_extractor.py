import re


COLORS = [
    "black",
    "white",
    "blue",
    "red",
    "green",
    "yellow",
    "grey",
    "gray",
    "pink",
    "purple",
    "brown",
    "orange"
]


GENDER_PATTERNS = {
    "men's": "Men",
    "mens": "Men",
    "men": "Men",
    "male": "Men",
    "women's": "Women",
    "womens": "Women",
    "women": "Women",
    "female": "Women",
    "unisex": "Unisex"
}


def extract_color(text: str):

    text = text.lower()

    for color in COLORS:

        if re.search(
            rf"\b{re.escape(color)}\b",
            text
        ):
            return color.title()

    return None


def extract_gender(text: str):

    text = text.lower()

    for pattern, value in GENDER_PATTERNS.items():

        if re.search(
            rf"\b{re.escape(pattern)}\b",
            text
        ):
            return value

    return None


def extract_size(text: str):

    patterns = [
        r"\bsize\s+(\d+(?:\.\d+)?)\b",
        r"\bsize\s+([XSML]{1,3})\b"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return None


def extract_attributes(
    title: str,
    description: str = ""
):

    combined_text = (
        f"{title} {description}"
    )

    return {
        "color": extract_color(
            combined_text
        ),
        "gender": extract_gender(
            combined_text
        ),
        "size": extract_size(
            combined_text
        )
    }
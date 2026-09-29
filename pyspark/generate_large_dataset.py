import csv
import random
from pathlib import Path


brands = [
    "Nike",
    "Adidas",
    "Puma",
    "Levi's",
    "Samsung",
    "Apple",
    "Sony",
    "LG",
    "Dell",
    "HP"
]


products = [
    "Running Shoes",
    "Sneakers",
    "Jeans",
    "T-Shirt",
    "Leggings",
    "Smartphone",
    "Television",
    "Laptop",
    "Headphones"
]


colors = [
    "Black",
    "White",
    "Blue",
    "Red",
    "Green"
]


output = Path(
    "data/raw/products_100k.csv"
)


with output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "product_id",
        "title",
        "description",
        "brand",
        "price"
    ])

    for i in range(100000):

        brand = random.choice(
            brands
        )

        product = random.choice(
            products
        )

        color = random.choice(
            colors
        )

        title = (
            f"{brand} "
            f"{product} "
            f"{color}"
        )

        description = (
            f"{brand} {product} "
            f"for everyday use"
        )

        price = round(
            random.uniform(
                20,
                1500
            ),
            2
        )

        writer.writerow([
            f"P{i + 1:06d}",
            title,
            description,
            brand,
            price
        ])


print(
    "100,000 product dataset created."
)
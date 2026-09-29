import csv
from pathlib import Path


products = [
    ("Nike", "Men's Running Shoes", "Running shoes for men"),
    ("Adidas", "Women's Running Shoes", "Running shoes for women"),
    ("Puma", "Men's Sneakers", "Casual sneakers for men"),
    ("Nike", "Women's Sneakers", "Lifestyle sneakers for women"),
    ("Levi's", "Men's Blue Jeans", "Classic denim jeans for men"),
    ("Levi's", "Women's Blue Jeans", "Classic denim jeans for women"),
    ("Nike", "Men's T-Shirt", "Cotton sports t-shirt"),
    ("Adidas", "Women's Leggings", "Athletic leggings"),
    ("Samsung", "55 Inch 4K Smart TV", "4K smart television"),
    ("LG", "65 Inch OLED TV", "OLED television"),
    ("Apple", "iPhone 15 Smartphone", "Apple smartphone"),
    ("Samsung", "Galaxy Smartphone", "Android smartphone"),
    ("Dell", "Inspiron Laptop", "Windows laptop"),
    ("HP", "Pavilion Laptop", "Windows notebook"),
    ("Sony", "Wireless Headphones", "Bluetooth headphones"),
    ("Apple", "AirPods Wireless Headphones", "Wireless audio headphones")
]

colors = [
    "Black",
    "White",
    "Blue",
    "Red",
    "Green"
]

output_file = Path(__file__).parent / "products.csv"

with output_file.open(
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
        "price",
        "category",
        "subcategory"
    ])

    product_number = 1

    for brand, product, description in products:

        for color in colors:

            product_id = f"P{product_number:04d}"

            title = f"{brand} {product} {color}"

            price = 50 + (product_number * 17) % 900

            product_lower = product.lower()

            if "shoe" in product_lower:
                category = "Footwear"

                if "running" in product_lower:
                    subcategory = "Running"
                else:
                    subcategory = "Casual"

            elif any(
                word in product_lower
                for word in [
                    "jeans",
                    "t-shirt",
                    "leggings"
                ]
            ):
                category = "Apparel"

                if "jeans" in product_lower:
                    subcategory = "Jeans"
                elif "leggings" in product_lower:
                    subcategory = "Activewear"
                else:
                    subcategory = "Shirts"

            elif any(
                word in product_lower
                for word in [
                    "tv",
                    "television"
                ]
            ):
                category = "Electronics"
                subcategory = "Television"

            elif "smartphone" in product_lower:
                category = "Electronics"
                subcategory = "Smartphones"

            elif "laptop" in product_lower:
                category = "Electronics"
                subcategory = "Laptops"

            elif "headphones" in product_lower:
                category = "Electronics"
                subcategory = "Audio"

            else:
                category = "Other"
                subcategory = "Other"

            writer.writerow([
                product_id,
                title,
                description,
                brand,
                price,
                category,
                subcategory
            ])

            product_number += 1

print(f"Dataset created: {output_file}")
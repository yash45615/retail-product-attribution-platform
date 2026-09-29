from pathlib import Path
import pandas as pd


# Project root:
# D:\retail-product-attribution-platform
ROOT_DIR = Path(__file__).resolve().parents[3]


def clean_products(input_file: str, output_file: str):
    print(f"Reading input file: {input_file}")

    # Read CSV
    df = pd.read_csv(input_file)

    # Remove duplicate product IDs
    if "product_id" in df.columns:
        df = df.drop_duplicates(subset=["product_id"])

    # Clean text columns
    text_columns = ["title", "description", "brand"]

    for column in text_columns:
        if column in df.columns:
            df[column] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.strip()
            )

    # Convert price to numeric
    if "price" in df.columns:
        df["price"] = pd.to_numeric(
            df["price"],
            errors="coerce"
        )

    # Remove products with empty titles
    if "title" in df.columns:
        df = df[df["title"] != ""]

    # Create output directory
    Path(output_file).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned data
    df.to_csv(output_file, index=False)

    print("Cleaning completed.")
    print(f"Rows after cleaning: {len(df)}")
    print(f"Output file: {output_file}")

    return df


if __name__ == "__main__":

    input_file = (
        ROOT_DIR
        / "data"
        / "raw"
        / "products.csv"
    )

    output_file = (
        ROOT_DIR
        / "data"
        / "processed"
        / "clean_products.csv"
    )

    clean_products(
        str(input_file),
        str(output_file)
    )
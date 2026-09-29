import json


class CustomerMapper:

    def __init__(
        self,
        taxonomy_file: str
    ):

        with open(
            taxonomy_file,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(file)

    def get_customer_name(self):

        return self.data.get(
            "customer",
            "Unknown"
        )

    def map_category(
        self,
        category: str,
        subcategory: str
    ):

        mapping = self.data.get(
            "mapping",
            {}
        )

        category_mapping = mapping.get(
            category,
            {}
        )

        return category_mapping.get(
            subcategory,
            "Unmapped"
        )
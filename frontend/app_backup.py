import requests
import streamlit as st
import pandas as pd


API_URL = (
    "http://127.0.0.1:8000"
)


st.set_page_config(
    page_title=(
        "Retail Product Attribution"
    ),
    page_icon="🛒",
    layout="wide"
)


st.title(
    "🛒 Retail Product Attribution "
    "Intelligence Platform"
)


st.write(
    "ML-assisted product attribution "
    "with automated extraction, "
    "confidence scoring and "
    "human-in-the-loop review."
)


st.sidebar.header(
    "Product"
)


product_id = st.sidebar.text_input(
    "Product ID",
    "P001"
)


title = st.sidebar.text_input(
    "Product Title",
    "Nike Men's Running Shoes Black Size 10"
)


description = st.sidebar.text_area(
    "Description",
    "Performance running shoes for men"
)


if st.sidebar.button(
    "Run Attribution"
):

    payload = {
        "product_id": product_id,
        "title": title,
        "description": description
    }

    try:

        response = requests.post(
            f"{API_URL}/api/attribute",
            json=payload,
            timeout=30
        )

        if response.status_code != 200:

            st.error(
                response.text
            )

        else:

            data = response.json()

            st.success(
                "Attribution completed."
            )

            col1, col2, col3 = (
                st.columns(3)
            )

            with col1:

                st.metric(
                    "Product Type",
                    data["product_type"]
                )

            with col2:

                st.metric(
                    "Category",
                    data[
                        "predicted_category"
                    ]
                )

            with col3:

                st.metric(
                    "Confidence",
                    f"{data['confidence']:.2%}"
                )

            st.subheader(
                "Extracted Attributes"
            )

            attributes = data[
                "attributes"
            ]

            attribute_df = pd.DataFrame(
                [
                    {
                        "Attribute": key,
                        "Value": value
                    }
                    for key, value
                    in attributes.items()
                ]
            )

            st.dataframe(
                attribute_df,
                use_container_width=True
            )

            st.subheader(
                "Review Decision"
            )

            if data["review_required"]:

                st.warning(
                    "⚠️ Human review required"
                )

            else:

                st.success(
                    "✅ Automatically approved"
                )

    except requests.RequestException as error:

        st.error(
            f"API connection failed: {error}"
        )
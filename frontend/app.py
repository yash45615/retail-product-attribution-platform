import requests
import streamlit as st
import pandas as pd


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Retail Product Attribution",
    page_icon="🛒",
    layout="wide"
)


st.title("🛒 Retail Product Attribution Intelligence Platform")

st.write(
    "ML-assisted product attribution with automated extraction, "
    "confidence scoring and human-in-the-loop review."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Single Product",
        "Batch Attribution",
        "Review Queue",
        "Analytics"
    ]
)


# ============================================================
# SINGLE PRODUCT
# ============================================================

if page == "Single Product":

    st.header("🔍 Single Product Attribution")

    st.sidebar.subheader("Product")

    product_id = st.sidebar.text_input(
        "Product ID",
        "P0001"
    )

    title = st.sidebar.text_input(
        "Product Title",
        "Nike Men's Running Shoes Black Size 10"
    )

    description = st.sidebar.text_area(
        "Description",
        "Performance running shoes for men"
    )

    if st.sidebar.button("Run Attribution"):

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

                st.error(response.text)

            else:

                data = response.json()

                st.success("Attribution completed.")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Product Type",
                        data["product_type"]
                    )

                with col2:
                    st.metric(
                        "Category",
                        data["predicted_category"]
                    )

                with col3:
                    st.metric(
                        "Confidence",
                        f"{data['confidence']:.2%}"
                    )

                st.subheader("Extracted Attributes")

                attributes = data["attributes"]

                attribute_df = pd.DataFrame(
                    [
                        {
                            "Attribute": key,
                            "Value": value
                        }
                        for key, value in attributes.items()
                    ]
                )

                st.dataframe(
                    attribute_df,
                    use_container_width=True
                )

                st.subheader("Review Decision")

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


# ============================================================
# BATCH ATTRIBUTION
# ============================================================

elif page == "Batch Attribution":

    st.header("📦 Batch Product Attribution")

    st.write(
        "Process all products from the retail product dataset "
        "through the attribution pipeline."
    )

    st.info(
        "The backend will read data/raw/products.csv and "
        "process all available products."
    )

    if st.button(
        "🚀 Process All Products",
        type="primary"
    ):

        with st.spinner(
            "Processing products..."
        ):

            try:

                response = requests.get(
                    f"{API_URL}/api/attribute/batch",
                    timeout=120
                )

                if response.status_code != 200:

                    st.error(
                        f"Batch API error: {response.text}"
                    )

                else:

                    data = response.json()

                    if "error" in data:

                        st.error(
                            data["error"]
                        )

                    else:

                        results = data.get(
                            "results",
                            []
                        )

                        if not results:

                            st.warning(
                                "No products were returned."
                            )

                        else:

                            # Store results in session
                            st.session_state[
                                "batch_results"
                            ] = results

                            st.success(
                                f"Successfully processed "
                                f"{len(results)} products."
                            )


            except requests.RequestException as error:

                st.error(
                    f"API connection failed: {error}"
                )


    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    if "batch_results" in st.session_state:

        results = st.session_state[
            "batch_results"
        ]

        df = pd.DataFrame(results)

        total_products = len(df)

        human_review = int(
            df["review_required"].sum()
        )

        auto_approved = (
            total_products - human_review
        )

        average_confidence = (
            df["confidence"].mean()
        )

        st.subheader(
            "Batch Summary"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Products",
                total_products
            )

        with col2:

            st.metric(
                "Auto Approved",
                auto_approved
            )

        with col3:

            st.metric(
                "Human Review",
                human_review
            )

        with col4:

            st.metric(
                "Average Confidence",
                f"{average_confidence:.2%}"
            )

        st.subheader(
            "Attribution Results"
        )

        display_columns = [
            "product_id",
            "title",
            "brand",
            "product_type",
            "predicted_category",
            "confidence",
            "review_required",
            "status"
        ]

        available_columns = [
            column
            for column in display_columns
            if column in df.columns
        ]

        display_df = df[
            available_columns
        ].copy()

        if "confidence" in display_df.columns:

            display_df[
                "confidence"
            ] = display_df[
                "confidence"
            ].round(4)

        st.dataframe(
            display_df,
            use_container_width=True,
            height=600
        )

        # ----------------------------------------------------
        # DOWNLOAD
        # ----------------------------------------------------

        csv = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇️ Download Attribution Results",
            data=csv,
            file_name="attribution_results.csv",
            mime="text/csv"
        )


# ============================================================
# REVIEW QUEUE
# ============================================================

elif page == "Review Queue":

    st.header("👤 Human Review Queue")

    if st.button("🔄 Refresh Review Queue"):

        try:

            response = requests.get(
                f"{API_URL}/api/reviews",
                timeout=30
            )

            if response.status_code != 200:

                st.error(
                    response.text
                )

            else:

                data = response.json()

                items = data.get(
                    "items",
                    []
                )

                if items:

                    review_df = pd.DataFrame(
                        items
                    )

                    st.metric(
                        "Review Items",
                        len(items)
                    )

                    st.dataframe(
                        review_df,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "No products are currently "
                        "in the review queue."
                    )

        except requests.RequestException as error:

            st.error(
                f"API connection failed: {error}"
            )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.header("📊 Attribution Analytics")

    if st.button("🔄 Refresh Analytics"):

        try:

            response = requests.get(
                f"{API_URL}/api/analytics",
                timeout=30
            )

            if response.status_code != 200:

                st.error(
                    response.text
                )

            else:

                data = response.json()

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Total",
                        data.get("total", 0)
                    )

                with col2:

                    st.metric(
                        "Pending",
                        data.get("pending", 0)
                    )

                with col3:

                    st.metric(
                        "Auto Approved",
                        data.get("auto_approved", 0)
                    )

                with col4:

                    st.metric(
                        "Manually Approved",
                        data.get(
                            "manually_approved",
                            0
                        )
                    )

        except requests.RequestException as error:

            st.error(
                f"API connection failed: {error}"
            )
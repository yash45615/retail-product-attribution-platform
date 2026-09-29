# 🛒 Retail Product Attribution Intelligence Platform

An end-to-end **ML-assisted retail product attribution platform** designed to automate product categorization, extract product attributes, map products to customer-specific taxonomies, assign confidence scores, and route low-confidence predictions to a **human review workflow**.

The platform combines **Python, Pandas, scikit-learn, Regex, PySpark, PostgreSQL, FastAPI, Streamlit, and Pytest** into a complete retail data-processing and product-attribution pipeline.

---

## 🚀 Project Overview

Retail datasets often contain inconsistent product descriptions, incomplete categorization, different naming conventions, and customer-specific category structures.

This project addresses that problem through a hybrid attribution pipeline:

```text
Raw Retail Product Data
        │
        ▼
Data Cleaning
        │
        ▼
Regex Attribute Extraction
        │
        ├── Color
        ├── Gender
        └── Size
        │
        ▼
Product Type Detection
        │
        ▼
ML Product Classification
        │
        ▼
Confidence Scoring
        │
        ├── High Confidence
        │       └── Auto Approved
        │
        └── Low Confidence
                └── Human Review
                        │
                        ▼
                Customer Taxonomy Mapping
                        │
                        ▼
                    PostgreSQL
                        │
                        ▼
                FastAPI + Streamlit
```

---

# ✨ Key Features

### 📦 Product Attribution

* Product type extraction using rule-based Regex
* ML-based product category classification
* Automated product categorization
* Confidence scoring for every prediction

### 🔎 Attribute Extraction

Automatically extracts attributes from product titles and descriptions:

* Color
* Gender
* Size
* Product type

Example:

```text
Nike Men's Running Shoes Black Size 10
```

Can produce:

```text
Product Type: Running Shoes
Gender: Men
Color: Black
Size: 10
Category: Footwear
```

---

### 🤖 Machine Learning Classification

The project uses a machine-learning pipeline based on:

* TF-IDF vectorization
* Unigrams and bigrams
* Logistic Regression
* Probability-based confidence scoring

The model learns from historical product data and predicts the appropriate product category.

---

### 🧠 Hybrid Attribution Engine

The platform combines deterministic rules with machine learning.

```text
                 Product
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   Regex Extraction       ML Model
          │                   │
          ├── Color           ├── Category
          ├── Gender          └── Confidence
          └── Size
                  │
                  ▼
          Hybrid Attribution
                  │
                  ▼
          Final Prediction
```

This approach allows structured attributes to be extracted deterministically while using ML for category classification.

---

### 👤 Human-in-the-Loop Review

Predictions are automatically evaluated using a confidence threshold.

Current threshold:

```text
80%
```

If:

```text
confidence >= 80%
```

the prediction can be automatically approved.

If:

```text
confidence < 80%
```

the product is routed to human review.

Example:

```text
Prediction:
Category: Electronics
Confidence: 62%

Status:
PENDING → Human Review
```

This helps prevent low-confidence predictions from being blindly accepted.

---

### 🏷️ Customer-Specific Taxonomy Mapping

Different customers may organize the same product differently.

For example:

```text
Customer A
Running Shoes → Running

Customer B
Running Shoes → Athletic
```

The platform supports customer-specific taxonomy files so the same product can be mapped according to different customer category structures.

---

### 📊 Batch Attribution

The platform can process the complete product dataset through a single API request.

Example:

```text
80 Products
      │
      ▼
Batch Attribution
      │
      ├── Product Classification
      ├── Attribute Extraction
      ├── Confidence Scoring
      └── Review Assignment
```

Batch results can also be downloaded as CSV from the Streamlit interface.

---

### 📋 Review Queue

The application provides a review workflow for products requiring human validation.

Review statuses include:

```text
PENDING
AUTO_APPROVED
APPROVED
```

Human reviewers can provide:

* Reviewer name
* Corrected category
* Corrected subcategory

---

### 📈 Analytics

The platform provides attribution workflow metrics such as:

* Total products
* Pending reviews
* Automatically approved products
* Manually approved products
* Average model confidence

---

# 🖥️ Application

The Streamlit application contains four major modules:

```text
┌─────────────────────────────────────┐
│ Retail Product Attribution Platform │
├─────────────────────────────────────┤
│                                     │
│  1. Single Product                  │
│  2. Batch Attribution               │
│  3. Review Queue                    │
│  4. Analytics                       │
│                                     │
└─────────────────────────────────────┘
```

---

# 🏗️ Technology Stack

## Programming

* Python 3.10
* SQL
* Regex

## Data Processing

* Pandas
* NumPy
* PySpark

## Machine Learning

* scikit-learn
* TF-IDF
* Logistic Regression
* Joblib

## Backend

* FastAPI
* Pydantic

## Database

* PostgreSQL

## Frontend

* Streamlit

## Testing

* Pytest

## Development

* Git
* GitHub
* VS Code

---

# 📁 Project Structure

```text
retail-product-attribution-platform/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   ├── attribution/
│   │   ├── core/
│   │   ├── db/
│   │   ├── ml/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │
│   ├── requirements.txt
│   └── venv/
│
├── data/
│   ├── raw/
│   │   ├── products.csv
│   │   └── products_100k.csv
│   │
│   ├── processed/
│   │   └── clean_products.csv
│   │
│   └── taxonomies/
│       ├── canonical_categories.json
│       ├── customer_a.json
│       ├── customer_b.json
│       └── customer_mappings.json
│
├── frontend/
│   └── app.py
│
├── pyspark/
│
├── sql/
│
├── docs/
│
├── .github/
│
├── .gitignore
├── pytest.ini
└── README.md
```

---

# 🔄 Data Processing Pipeline

## Step 1 — Raw Data

The platform starts with retail product data containing fields such as:

```text
product_id
title
description
brand
price
category
subcategory
```

Example:

```text
P0001
Nike Men's Running Shoes Black
Nike
Footwear
Running
```

---

## Step 2 — Data Cleaning

The cleaning pipeline:

* Removes duplicate product IDs
* Handles missing text values
* Converts price values to numeric format
* Removes invalid records
* Standardizes text fields

Output:

```text
data/processed/clean_products.csv
```

---

## Step 3 — Attribute Extraction

Regex-based extraction identifies structured attributes from unstructured product text.

Example:

```text
Nike Women's Running Shoes Blue Size 8
```

Output:

```json
{
  "color": "Blue",
  "gender": "Women",
  "size": "8"
}
```

---

## Step 4 — Product Type Detection

The rule-based product type engine identifies products such as:

```text
Running Shoes
Sneakers
Jeans
T-Shirts
Leggings
Television
Smartphone
Laptop
Headphones
```

---

## Step 5 — Machine Learning Classification

Product title and description are combined:

```text
title + description
```

The text is transformed using:

```text
TF-IDF
```

and classified using:

```text
Logistic Regression
```

The model returns:

```text
Predicted Category
Confidence Score
```

---

# 🤖 Machine Learning Pipeline

```text
Product Text
     │
     ▼
Text Cleaning
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Logistic Regression
     │
     ▼
Category Prediction
     │
     ▼
Probability / Confidence
```

The trained model is saved locally as:

```text
product_classifier.joblib
```

Model artifacts are excluded from Git using `.gitignore`.

---

# 👤 Human Review Workflow

```text
ML Prediction
      │
      ▼
Confidence Score
      │
      ├───────────────┐
      │               │
      ▼               ▼
 >= 80%             < 80%
      │               │
      ▼               ▼
AUTO_APPROVED      PENDING
                      │
                      ▼
                 Human Review
                      │
                      ▼
                   APPROVED
```

---

# 🗂️ Customer Taxonomy

The platform supports different taxonomies for different customers.

Example:

### Customer A

```json
{
  "Running Shoes": "Running",
  "Sneakers": "Casual",
  "Smartphone": "Mobile Phones"
}
```

### Customer B

```json
{
  "Running Shoes": "Athletic",
  "Sneakers": "Lifestyle",
  "Smartphone": "Smart Devices"
}
```

This demonstrates how product attribution can be adapted to customer-specific category structures.

---

# 🗄️ PostgreSQL Database

The application uses PostgreSQL for structured storage.

Current database entities include:

```text
customers
products
product_attributes
model_predictions
attributions
reviews
data_quality_results
```

The database supports storage of:

* Product information
* Extracted attributes
* ML predictions
* Confidence scores
* Attribution results
* Review records
* Customer information
* Data quality results

---

# ⚡ FastAPI Backend

The backend exposes REST APIs for the attribution platform.

Base URL:

```text
http://127.0.0.1:8000
```

## Health Check

```http
GET /health
```

Example:

```json
{
  "status": "healthy"
}
```

---

## Single Product Attribution

```http
POST /api/attribute
```

Example request:

```json
{
  "product_id": "P001",
  "title": "Nike Men's Running Shoes Black Size 10",
  "description": "Performance running shoes for men"
}
```

---

## Batch Attribution

```http
GET /api/attribute/batch
```

Processes all products from:

```text
data/raw/products.csv
```

---

## Create Review

```http
POST /api/reviews
```

Creates a review record for a product attribution.

---

## Review Queue

```http
GET /api/reviews
```

Returns current review records.

---

## Review Decision

```http
POST /api/reviews/decision
```

Allows a reviewer to approve or correct a prediction.

---

## Analytics

```http
GET /api/analytics
```

Returns review and attribution statistics.

---

# 📊 Streamlit Dashboard

The frontend provides an interactive interface for the attribution workflow.

### Single Product

Run attribution on an individual product.

### Batch Attribution

Process the complete product dataset and download results.

### Review Queue

View products requiring review and their prediction information.

### Analytics

View workflow-level attribution metrics.

---

# 🧪 Testing

The project uses Pytest for backend testing.

Run:

```powershell
pytest -v
```

The test suite covers backend functionality such as:

* API endpoints
* Attribution logic
* Product processing
* Review functionality
* Data processing

---

# ▶️ How to Run the Project

## 1. Clone the repository

```powershell
git clone https://github.com/YOUR_USERNAME/retail-product-attribution-platform.git
```

```powershell
cd retail-product-attribution-platform
```

---

# 2. Create the Python environment

```powershell
cd backend
```

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 4. Start PostgreSQL

Make sure PostgreSQL is running and the required database exists.

Example database:

```text
retail_attribution_db
```

Configure your local database connection through your environment configuration.

Do not commit credentials or `.env` files.

---

# 5. Start FastAPI

From:

```text
backend/
```

run:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 6. Start Streamlit

Open another PowerShell terminal.

```powershell
cd D:\retail-product-attribution-platform\frontend
```

Run:

```powershell
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

# 7. Run Tests

From the project root:

```powershell
cd D:\retail-product-attribution-platform
```

Run:

```powershell
pytest -v
```

---

# 🔐 Security

Sensitive configuration is excluded from Git.

The project `.gitignore` excludes:

```text
.env
venv/
__pycache__/
*.joblib
*.pkl
.pytest_cache/
.vscode/
```

Never commit:

* API keys
* Database passwords
* Access tokens
* Private credentials
* Production secrets

---

# 📈 Scalability

The project also includes a PySpark processing workflow for larger datasets.

The intended scalable pipeline is:

```text
Large Retail Dataset
        │
        ▼
      PySpark
        │
        ▼
Data Cleaning
        │
        ▼
Feature Processing
        │
        ▼
Attribution Pipeline
```

A synthetic dataset containing 100,000 product records was also created to demonstrate large-scale processing.

---

# 🎯 Business Use Cases

This platform can support retail data workflows such as:

* Product categorization
* Product taxonomy mapping
* Catalog normalization
* Product attribute extraction
* Customer-specific classification
* Data quality workflows
* ML-assisted tagging
* Human-in-the-loop data validation
* Retail catalog enrichment
* Automated product attribution

---

# 💡 Example Attribution

### Input

```text
Product ID:
P0001

Title:
Nike Men's Running Shoes Black Size 10

Description:
Performance running shoes designed for daily training.
```

### Extracted Information

```text
Product Type: Running Shoes
Gender: Men
Color: Black
Size: 10
```

### ML Result

```text
Predicted Category: Footwear
Confidence: 95%
```

### Workflow Decision

```text
Confidence >= 80%
        ↓
AUTO_APPROVED
```

For a lower-confidence prediction:

```text
Confidence < 80%
        ↓
PENDING
        ↓
Human Review
```

---

# 🧩 Design Principles

The project was designed around several practical data-engineering and ML principles:

### Automation

Automate repetitive product classification and attribute extraction.

### Explainability

Expose extracted attributes, predicted categories, and confidence scores.

### Human Oversight

Use human review for low-confidence predictions rather than automatically accepting every ML output.

### Customer Adaptability

Support different customer-specific product taxonomies.

### Scalability

Use Pandas for standard workloads and PySpark for larger datasets.

### API-First Architecture

Expose attribution functionality through FastAPI so other systems can consume the platform.

---

# 🔮 Future Improvements

Planned improvements include:

* Persistent review workflow using PostgreSQL
* Advanced customer taxonomy mapping
* Product similarity matching
* Embedding-based semantic classification
* LLM-assisted product attribution
* Active learning from reviewer corrections
* Model performance monitoring
* Precision/recall/F1 dashboards
* Data quality monitoring
* Role-based reviewer authentication
* Background batch processing
* Production deployment
* Automated CI/CD pipeline
* Larger real-world retail datasets

---

# 👨‍💻 Author

**Yash Kalbhile**

GitHub:

https://github.com/yash45615

---

# ⭐ Project Highlights

```text
✓ End-to-end retail product attribution pipeline
✓ Python-based data processing
✓ Regex attribute extraction
✓ Machine learning classification
✓ TF-IDF + Logistic Regression
✓ Confidence scoring
✓ Human-in-the-loop review
✓ Customer-specific taxonomy mapping
✓ PostgreSQL database
✓ FastAPI REST API
✓ Streamlit dashboard
✓ PySpark large-scale processing
✓ Pytest testing
✓ GitHub-based version control
```

---

## 📌 Portfolio Project

This project demonstrates practical skills across:

```text
Data Processing
      +
Machine Learning
      +
Product Attribution
      +
Data Quality
      +
SQL / PostgreSQL
      +
API Development
      +
Dashboard Development
      +
Scalable Data Processing
      +
Testing
```

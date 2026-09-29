CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    taxonomy_file VARCHAR(255)
);


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(100) UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    brand VARCHAR(100),
    price NUMERIC(10,2)
);


CREATE TABLE product_attributes (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    color VARCHAR(50),
    gender VARCHAR(50),
    size VARCHAR(50),
    product_type VARCHAR(100)
);


CREATE TABLE model_predictions (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    predicted_category VARCHAR(100),
    confidence NUMERIC(6,5),
    review_required BOOLEAN
);


CREATE TABLE attributions (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    customer_id INTEGER REFERENCES customers(id),
    category VARCHAR(100),
    subcategory VARCHAR(100),
    final_status VARCHAR(50)
);


CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    reviewer VARCHAR(100),
    corrected_category VARCHAR(100),
    corrected_subcategory VARCHAR(100),
    status VARCHAR(50)
);
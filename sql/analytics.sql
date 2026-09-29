-- Total products

SELECT COUNT(*) AS total_products
FROM products;


-- Unique products

SELECT COUNT(DISTINCT product_id)
FROM products;


-- Products by brand

SELECT
    brand,
    COUNT(*) AS product_count
FROM products
GROUP BY brand
ORDER BY product_count DESC;


-- Predictions by category

SELECT
    predicted_category,
    COUNT(*) AS prediction_count
FROM model_predictions
GROUP BY predicted_category
ORDER BY prediction_count DESC;


-- Average confidence

SELECT
    AVG(confidence)
FROM model_predictions;


-- Low confidence predictions

SELECT
    COUNT(*)
FROM model_predictions
WHERE confidence < 0.80;


-- Review status

SELECT
    status,
    COUNT(*)
FROM reviews
GROUP BY status;
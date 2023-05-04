SELECT
    customer.full_name AS buyer,
    order_db.order_no
FROM 'order' AS order_db
INNER JOIN customer
    ON order_db.customer_id = customer.customer_id
WHERE order_db.manager_id IS NULL;
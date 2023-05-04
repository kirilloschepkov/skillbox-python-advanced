SELECT
    order_db.order_no,
    manager.full_name AS seller,
    customer.full_name AS buyer
FROM 'order' AS order_db
INNER JOIN customer
    ON order_db.customer_id = customer.customer_id
INNER JOIN manager
    ON manager.manager_id = order_db.manager_id
WHERE customer.city != manager.city;
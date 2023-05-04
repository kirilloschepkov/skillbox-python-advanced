SELECT
    customer.full_name AS buyer,
    manager.full_name AS seller,
    purchase_amount AS amount,
    date
FROM 'order'
INNER JOIN customer
    ON 'order'.customer_id = customer.customer_id
INNER JOIN manager
    ON 'order'.manager_id = manager.manager_id;
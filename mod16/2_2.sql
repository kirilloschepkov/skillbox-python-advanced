SELECT customer.full_name AS buyer_without_orders
FROM customer
LEFT JOIN 'order'
    ON 'order'.customer_id = customer.customer_id
WHERE 'order'.order_no IS NULL;
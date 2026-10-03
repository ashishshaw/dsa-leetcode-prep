--Approach: Use a subquery to assign a row number to each order for each customer, ordered by order date in descending order.
--Then filter the results to include only the latest order for each customer (i.e., rows with row number equal to 1).

SELECT *
FROM (
    SELECT o.*,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY order_date DESC
           ) AS rn
    FROM orders o
) t
WHERE rn = 1;

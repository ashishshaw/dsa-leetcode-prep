--Approach: Use a LEFT JOIN to join the Customers table with the Orders table on the customerId.
--Filter the results to include only those customers who do not have any matching records in the Orders table 
-- (i.e., customers who have never placed an order).

SELECT
    c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL
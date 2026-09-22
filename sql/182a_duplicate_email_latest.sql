--Approach: Use the ROW_NUMBER() window function to assign a unique number to each row within each email group, 
--ordered by the updated_at column in descending order. Then filter the results to include only the rows with a row number 
--greater than 1, indicating duplicate emails.


SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY email
               ORDER BY updated_at DESC
           ) AS rn
    FROM employees e
) t
WHERE rn > 1;

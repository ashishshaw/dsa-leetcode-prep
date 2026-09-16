--Query to find the second highest salary in each department from the Employee table using DENSE_RANK() function
--to rank the salaries within each department and then filtering the results to get only the second highest salary for each department.

SELECT salary, department
FROM (
    SELECT DISTINCT
           salary,
           department,
           DENSE_RANK() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rnk
    FROM employee
) t
WHERE rnk = 2;
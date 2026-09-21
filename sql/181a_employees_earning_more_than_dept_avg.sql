--Approach: Use a subquery to calculate the average salary for each department using the AVG() window function.
--Then filter the employees whose salary is greater than the average salary of their respective department.

SELECT *
FROM (
    SELECT e.*,
           AVG(salary) OVER (
               PARTITION BY department_id
           ) AS dept_avg
    FROM employees e
) t
WHERE salary > dept_avg;

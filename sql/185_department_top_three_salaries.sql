--Query to find the top three salaries in each department from the Employee table using DENSE_RANK() function 
--to rank the salaries within each department and then filtering the results to get only the top three salaries for each department.

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
) t
WHERE rnk <= 3;
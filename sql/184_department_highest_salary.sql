--Subquery to get the maximum salary for each department and then join it with the Employee and Department tables to get the required details.
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
JOIN 
    Department d
ON 
    e.departmentId = d.id
WHERE 
    (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
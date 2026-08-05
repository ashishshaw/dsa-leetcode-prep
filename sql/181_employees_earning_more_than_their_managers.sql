--Approach: Join the Employee table with itself to compare the salaries of employees and their managers. 
--Filter the results to include only those employees whose salary is greater than their manager's salary.

SELECT
    e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;
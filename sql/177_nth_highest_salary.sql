

SELECT 
    s.salary
FROM (
        SELECT DISTINCT e.salary, DENSE_RANK() OVER (ORDER BY e.salary DESC) AS rank
        FROM Employee e
    ) s
WHERE s.rank = N

SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET N-1;

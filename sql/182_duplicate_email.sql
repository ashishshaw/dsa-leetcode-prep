--Approach: Use the GROUP BY clause to group the records by email and then use the HAVING clause to filter out the groups that have a count greater than 1, indicating duplicate emails.

SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1
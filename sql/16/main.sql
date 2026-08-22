SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    (
        SELECT
            *,
            DENSE_RANK() OVER (
                PARTITION BY departmentID
                ORDER BY salary DESC
            ) AS salary_rank
        FROM Employee
    ) e
JOIN Department d
    ON e.departmentID = d.id
WHERE e.salary_rank <= 3
;
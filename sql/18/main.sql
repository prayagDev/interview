# Write your MySQL query statement below
WITH s AS (
    SELECT
        *,
        LAG(id, 1) OVER (ORDER BY id) AS prev1,
        LAG(id, 2) OVER (ORDER BY id) AS prev2,
        LEAD(id, 1) OVER (ORDER BY id) AS next1,
        LEAD(id, 2) OVER (ORDER BY id) AS next2
    FROM Stadium
    WHERE people >= 100
)
SELECT
    id,
    visit_date,
    people
FROM s
WHERE
       (prev1 = id - 1 AND prev2 = id - 2)
    OR (prev1 = id - 1 AND next1 = id + 1)
    OR (next1 = id + 1 AND next2 = id + 2)
ORDER BY visit_date
;
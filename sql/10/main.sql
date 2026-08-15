SELECT
    d1.visited_on,
    SUM(d2.daily_amount) AS amount,
    ROUND((SUM(d2.daily_amount) / 7), 2) AS average_amount
FROM
    (
        SELECT
            visited_on,
            SUM(amount) as daily_amount
        FROM Customer
        GROUP BY visited_on
    ) d1
JOIN
    (
        SELECT
            visited_on,
            SUM(amount) as daily_amount
        FROM Customer
        GROUP BY visited_on
    ) d2
ON  
    d2.visited_on
        BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 Day)
        AND d1.visited_on

GROUP BY d1.visited_on

HAVING COUNT(*) = 7

ORDER BY d1.visited_on
;
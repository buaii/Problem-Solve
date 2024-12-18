WITH fish AS (
    SELECT 
        CASE
            WHEN length <= 10 THEN 10
            when length is null then 10
            ELSE length
        END AS AVERAGE_LENGTH
    FROM fish_info
)

SELECT 
    ROUND(AVG(AVERAGE_LENGTH), 2) AS AVERAGE_LENGTH
FROM fish

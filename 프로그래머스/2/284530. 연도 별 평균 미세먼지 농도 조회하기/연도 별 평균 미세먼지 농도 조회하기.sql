SELECT YEAR(YM) AS `year`, 
       round(AVG(PM_VAL1), 2) AS PM10, 
       ROUND(AVG(PM_VAL2), 2) AS `PM2.5`
FROM air_pollution
WHERE location2 = '수원'
GROUP BY YEAR(YM)
ORDER BY `year`;

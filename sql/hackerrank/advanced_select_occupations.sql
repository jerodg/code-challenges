SELECT MAX(Doctor)    AS Doctor,
       MAX(Professor) AS Professor,
       MAX(Singer)    AS Singer,
       MAX(Actor)     AS Actor
FROM (SELECT CASE WHEN Occupation = 'Doctor' THEN Name END             AS Doctor,
             CASE WHEN Occupation = 'Professor' THEN Name END          AS Professor,
             CASE WHEN Occupation = 'Singer' THEN Name END             AS Singer,
             CASE WHEN Occupation = 'Actor' THEN Name END              AS Actor,
             ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RowNumber
      FROM OCCUPATIONS) AS PivotTable
GROUP BY RowNumber
ORDER BY RowNumber;
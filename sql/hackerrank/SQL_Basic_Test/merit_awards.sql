SELECT e.employee_ID, e.name
FROM employee_information e
         JOIN last_quarter_bonus l ON e.employee_ID = l.employee_ID
WHERE e.division = 'HR'
  AND l.bonus >= 5000;
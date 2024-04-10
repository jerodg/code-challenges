SELECT s.roll_number, s.name
FROM student_information s
         JOIN faculty_information f ON s.advisor = f.employee_ID
WHERE (f.gender = 'M' AND f.salary > 15000)
   OR (f.gender = 'F' AND f.salary > 20000);
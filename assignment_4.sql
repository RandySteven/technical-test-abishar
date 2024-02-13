UPDATE FROM data_grade_employee
SET dge_salary = 15000
WHERE dge_salary BETWEEN 5000 AND 20000

SELECT de.de_position, COUNT(de.de_id), SUM(dge.dge_salary) FROM data_employee de JOIN data_grade_employee dge
ON de.de_id = dge.dge_de_id
WHERE de.de_position IN ('Staff', 'Kadiv')
GROUP BY de.de_position
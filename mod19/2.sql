SELECT
    full_name AS name,
    AVG(assignments_grades.grade) AS avg_grades
FROM students
JOIN assignments_grades
    ON students.student_id = assignments_grades.student_id
GROUP
    BY name
ORDER
    BY avg_grades DESC
LIMIT 10;

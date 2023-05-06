SELECT
    full_name AS name,
    AVG(assignments_grades.grade) AS avg_grade
FROM teachers
JOIN assignments
    ON teachers.teacher_id = assignments.teacher_id
JOIN assignments_grades
    ON assignments.assisgnment_id = assignments_grades.assisgnment_id
GROUP
    BY name
ORDER
    BY avg_grade
LIMIT 1;
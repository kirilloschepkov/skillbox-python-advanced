SELECT
    students.group_id,
    COUNT(DISTINCT students.student_id) AS count_students,
    AVG(assignments_grades.grade) AS avg_grade,
    COUNT(DISTINCT
        CASE
            WHEN assignments_grades.grade IS NULL
            THEN students.student_id
        END) AS ungraded_count_students,
    COUNT(DISTINCT
        CASE
            WHEN assignments_grades.date > assignments.due_date
            THEN students.student_id
        END) AS overdue_count_students,
    COUNT(DISTINCT assignments_grades.grade_id) AS attempts_count_students
FROM students
LEFT JOIN assignments_grades
    ON students.student_id = assignments_grades.student_id
LEFT JOIN assignments
    ON assignments_grades.assisgnment_id = assignments.assisgnment_id
GROUP BY students.group_id;
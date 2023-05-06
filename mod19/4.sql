SELECT
    group_id,
    AVG(count) AS avg,
    MAX(count) AS max,
    MIN(count) AS min
FROM (
    SELECT
        group_id,
        COUNT(grade) AS count
    FROM assignments_grades
    JOIN students
        ON assignments_grades.student_id = students.student_id
    WHERE grade = 0
    GROUP BY students.student_id, group_id
     )
GROUP BY group_id;
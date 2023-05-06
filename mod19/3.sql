SELECT DISTINCT full_name
FROM students
WHERE group_id IN
    (SELECT group_id
     FROM students_groups
     WHERE teacher_id IN
         (SELECT teacher_id
             FROM assignments
             WHERE assisgnment_id IN
                 (SELECT assisgnment_id
                  FROM assignments_grades
                  GROUP
                      BY assisgnment_id
                  ORDER
                      BY AVG(grade) DESC
                  LIMIT 1)))

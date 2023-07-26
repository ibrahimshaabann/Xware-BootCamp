# Task  : Using College Management System Database With Joins
  1. Select Subject id, Subject Name, Subject Code, Course Duration in One Query
  2. Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query
  3. Select All Students With Thier Address In one Query
  4. Select All Student Name In Every Couse.



1. Select Subject id, Subject Name, Subject Code, Course Duration in One Query

```sql
  SELECT Subjects.sub_id, Subjects.sub_name, Subjects.sub_code, course.duration
  FROM subjects 
  INNER JOIN course
  ON course.sub_id = subjects.sub_id;
```
  
2. Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query
```sql
SELECT subjects.sub_id, Subjects.sub_name, Subjects.sub_code, course.duration, Professor.F_Name, Professor.L_Name
FROM Professor 
FULL OUTER JOIN course  ON course.p_id = professor.p_id
FULL OUTER JOIN subjects ON course.sub_id = subjects.sub_id;
```

3. Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query
```sql
SELECT student.F_name,student.L_name,address.line_1
FROM student
left outer join Student_Address
on
 student.Stu_id = Student_Address.Stu_id
left outer join address
on
 address.A_id = Student_Address.A_id;
```

4. Select All Student Name In Every Couse.
```sql
SELECT student.stu_id, student.f_name, department.d_name , Subject.gvernorate, Address.city, Address.line_1, Student_Address.Stu_A_id
FROM student
INNER  JOIN department  ON Student_Address.stu_id = student.stu_id
INNER  JOIN Address ON Student_Address.a_id= Address.a_id,
INNER  JOIN Address ON Student_Address.a_id= Address.a_id;
```



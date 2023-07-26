# Different Types of SQL JOINs
## Here are the different types of the JOINs in SQL:

* (INNER) JOIN: Returns records that have matching values in both tables
* LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
* RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
* FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table


## examples on Inner join 

### Suppose you have the next Tables:
  * student (id, name)
  * course (id, name)
  * enrolment (id, student_id [FK], course_id [FK])
  


### Make Inner Join between student and enrolment
```
SELECT student.name AS stud_name, course.name AS cour_name, enrolment.id  AS enrolment_id
FROM student
JOIN enrolment ON student.id = enrolment.student_id
```

### Make Inner Join between the three tables
```
SELECT student.name AS stud_name, course.name AS cour_name, enrolment.id  AS enrolment_id
FROM student
JOIN enrolment ON student.id = enrolment.student_id
JOIN course ON course.id = enrolment.course_id;
```



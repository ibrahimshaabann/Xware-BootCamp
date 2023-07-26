* >>> - Select Data From Thse Tables.
 
### Select all Students, Professor, Subjects, Courses, Exams, Departments

```
SELECT * FROM student;
SELECT * FROM Professor;
SELECT * FROM Subjects;
SELECT * FROM Course;
SELECT * FROM Exams;
SELECT * FROM department;
```


### Select all Professors with the Age is 40

```
SELECT * FROM Professor WHERE age=40;
```
  
### Select all Professors with the salary greater than 10000

```
SELECT * FROM Professor WHERE Salary>10000;
```
  
### Order the Professors by the salary

```
SELECT * FROM Professor ORDER BY Salary ASC;
```
   
### Order the students by the Birth_Date

```
SELECT * FROM student ORDER BY Birth_date ASC;
```
  
### Get the average salary of the Professors

```
SELECT AVG(Salary) AS average_salary FROM Professor;
```
  
### Update the salary of the Professors with the salary greater than 10000 to 20000

```
UPDATE Professor set Salary = 20000 WHERE Salary >= 10000; 
```
  
### Delete the Professors with the salary greater than 20000

```
DELETE FROM Professor WHERE Salary >= 20000;
```
		
* >>> - Update These Tables
	
	
### Add Age Column in Student Table

```
ALTER TABLE Student ADD age INT NULL;
```
  
### Set Students Age

```
UPDATE Student SET age = 18 WHERE Stu_id<=5; 
UPDATE Student SET age = 20 WHERE Stu_id %2 = 0; 
UPDATE Student SET age = 22 WHERE Stu_id IN (7, 9, 11, 13); 
```
  
  
  
  
  

# Queries

## Note the following database

```sql
create table student(
    id int primary key not null,
    name varchar(20) not null,
    age int not null
);

create table course(
    id int primary key not null,
    name varchar(20) not null
);


create table enrolment(
    id int primary key not null,
    student_id int not null,
    course_id int not null
);



insert INTO student(id, name, age) values(1, 'Hady', 26);
insert INTO student(id, name, age) values(2, 'Eslam', 26);
insert INTO student(id, name, age) values(3, 'Mohammed', 26);
insert INTO student(id, name, age) values(4, 'Sadiq', 26);



INSERT into course(id, name) values(1, 'A');
INSERT into course(id, name) values(2, 'B');
INSERT into course(id, name) values(3, 'C');
INSERT into course(id, name) values(4, 'D');


insert into enrolment(id, student_id, course_id) values(1, 1, 1);
insert into enrolment(id, student_id, course_id) values(2, 1, 2);
insert into enrolment(id, student_id, course_id) values(3, 2, 1);
insert into enrolment(id, student_id, course_id) values(4, 3, 1);'
```


## practices on database

  1. Select All Students enrolled in Course B
  2. Select All Students enrolled in Course D
  3. Select All Courses has student "Hady" in them.
  4. Select All Courses has student "Sadiq" in them.



### Answers

> 1. Select All Students enrolled in Course B

```sql
select 
    enrolment.id,
    enrolment.student_id,
    enrolment.course_id,
    student.name,
    course.name

    from enrolment

    JOIN student
    on enrolment.student_id = student.id
    JOIN course
    on enrolment.course_id = course.id;
```

> 2. Select All Students enrolled in Course D
```sql
select

    enrolment.id,
    enrolment.student_id,
    enrolment.course_id,
    student.name

    from enrolment

    left JOIN student
    on enrolment.student_id = student.id;

```


> 3. Select All Courses has student "Hady" in them.
```sql
select

    enrolment.id,
    enrolment.student_id,
    enrolment.course_id,
    student.name

    from enrolment

    right JOIN student
     on enrolment.student_id = student.id;
```
> 4. Select All Courses has student "Sadiq" in them.

```sql
select

    enrolment.id,
    enrolment.student_id,
    enrolment.course_id,
    student.name

    from enrolment

    full OUTER JOIN student
    on enrolment.student_id = student.id;
```










   







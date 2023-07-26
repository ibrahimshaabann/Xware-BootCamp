# Exercise1

```sql
* CREATE TABLE Student (
  * Stu_id BIGINT PRIMARY KEY,
  * F_Name VARCHAR(15) NOT NULL,
  * L_Name VARCHAR(15) NOT NULL,
  * F_Phone VARCHAR(11) NOT NULL,
  *  L_Phone VARCHAR(11) NOT NULL,
  * Birth_date DATE NOT NULL,
  *  Stu_image TEXT NOT NULL 
* );

* CREATE TABLE Professor (
  *  P_id BIGINT PRIMARY KEY,
  * F_id BIGINT(15) NOT NULL,
  *  D_id BIGINT(15) NOT NULL,
  * F_Name VARCHAR(15) NOT NULL,
  *  L_Name VARCHAR(15) NOT NULL,
  * Age INT NOT NULL,
  *  Salary INT NOT NULL,
  * check (Age>=30),
  *  Prof_image TEXT NOT NULL 
* );

* CREATE TABLE Subjects (
  *  Sub_id BIGINT PRIMARY KEY,
  * Sub_name VARCHAR(15) NOT NULL,
  *  Sub_code VARCHAR(15) NOT NULL,
  * F_id BIGINT NOT NULL
* );

* CREATE TABLE Course (
  *  C_id BIGINT PRIMARY KEY,
  * Duration VARCHAR(10) NOT NULL,
  *  Sub_id BIGINT NOT NULL,
  * P_id BIGINT NOT NULL
* );

* CREATE TABLE faculty (
  *  F_id BIGINT PRIMARY KEY,
  * F_Name VARCHAR(15) NOT NULL
* );

* CREATE TABLE department (
  *  D_id BIGINT PRIMARY KEY,
  * D_Name VARCHAR(15) NOT NULL,
  *  F_id BIGINT NOT NULL 
* );

* CREATE TABLE Address ( 
  *  A_id BIGINT PRIMARY KEY,
  * Gvernorate VARCHAR(15) NOT NULL,
  *  City VARCHAR(15) NOT NULL,
  * line_1 VARCHAR(15) NOT NULL,
  *  line_2 VARCHAR(15) NULL
* );

* CREATE TABLE Student_Address ( 
  * Stu_A_id BIGINT PRIMARY KEY,y
  * A_id BIGINT NOT NUL
  * Stu_id BIGINT  NOT NULL
* );

CREATE TABLE Exams ( 
   * E_id BIGINT PRIMARY KEY,
   * C_id BIGINT  NOT NULL,
   * examDate DATE NOT NULL,
   * examTime TIME NOT NULL,
   * duration VARCHAR(10) NOT NULL
* );

* CREATE TABLE Course_Enrolment (
   * C_E_id BIGINT PRIMARY KEY,
   * C_id BIGINT NOT NULL,
   * Sub_id BIGINT NOT NULL
* );
```

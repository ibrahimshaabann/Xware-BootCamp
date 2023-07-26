# **Tasks**:

## Creating database and tables and relationships
* **CREATE DATABASE faculty_db;**

```sql
CREATE DATABASE faculty_db;
```

```sql
CREATE TABLE Student (
    Stu_id SERIAL PRIMARY KEY,
    F_Name VARCHAR(15) NOT NULL,
    L_Name VARCHAR(15) NOT NULL,
    F_Phone VARCHAR(11) NULL,
    L_Phone VARCHAR(11) NULL,
    Birth_date DATE ,
    Stu_image TEXT  ,
    Dep_id INT NOT NULL REFERENCES department(D_id)
);
```

```sql
CREATE TABLE Professor (
    P_id SERIAL PRIMARY KEY,
    Fac_id INT REFERENCES faculty(F_id),
    Dep_id INT REFERENCES department(D_id),
    F_Name VARCHAR(15) NOT NULL,
    L_Name VARCHAR(15) NOT NULL,
    Age INT NOT NULL,
    Salary INT NOT NULL,
    check (Age>=30),
    Prof_image TEXT NOT NULL 
);
```

```sql
CREATE TABLE Subjects (
    Sub_id SERIAL PRIMARY KEY,
    Sub_name VARCHAR(15) NOT NULL,
    Sub_code VARCHAR(15) NOT NULL,
    Dep_id INT NOT NULL REFERENCES department(D_id)
);
```

```sql
CREATE TABLE Course (
    C_id SERIAL PRIMARY KEY,
    Duration VARCHAR(10) NOT NULL,
    Sub_id INT NOT NULL REFERENCES Subjects(Sub_id),
    P_id INT NOT NULL REFERENCES Professor(P_id)
);
```

```sql
CREATE TABLE faculty (
    F_id SERIAL PRIMARY KEY,
    F_Name VARCHAR(15) NOT NULL
);
```

```sql
CREATE TABLE department (
    D_id SERIAL PRIMARY KEY,
    D_Name VARCHAR(15) NOT NULL,
    F_id INT NOT NULL REFERENCES faculty(F_id)
);
```

```sql
CREATE TABLE Address (   
    A_id SERIAL PRIMARY KEY,
    Gvernorate VARCHAR(15) NULL,
    City VARCHAR(15)  NULL,
    line_1 VARCHAR(15) NULL,
    line_2 VARCHAR(15) NULL
);
```

```sql
CREATE TABLE Student_Address (   
    Stu_A_id SERIAL PRIMARY KEY,
    A_id INT NOT NULL REFERENCES Address(A_id),
    Stu_id INT NOT NULL REFERENCES Student(Stu_id)
);
```

```sql
CREATE TABLE Exams (   
    E_id SERIAL PRIMARY KEY,
    Course_id INT NOT NULL REFERENCES Course(C_id),
    examDate DATE NULL,
    examTime TIME NULL,
    duration VARCHAR(10) NOT NULL
);
```

```sql
CREATE TABLE Course_Enrolment (
    C_E_id SERIAL PRIMARY KEY,
    C_id INT NOT NULL REFERENCES Course(C_id),
    Sub_id INT NOT NULL REFERENCES Subjects(Sub_id)
);
```







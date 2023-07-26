# Exercise 1
>>> - Insert Data Into These Tables.

## Insert One Faculty

```sql
INSERT INTO faculty (F_Name) VALUES
('FCI') ;
```
        
          
## Insert Three Departments Into This Faculty	
```sql
INSERT INTO department (D_Name, F_id) VALUES
('CS', 1) ,
('IS', 1) ,
('IT', 1) ;
```

## Insert Three Subjects In Every Department	

```sql
INSERT INTO Subjects (Sub_name, Sub_code, Dep_id) VALUES
('Algorithm', 'cs501', 1),
('Compiler', 'cs502', 1),
('Computer Vision', 'cs03', 1),
('GIS', 'is401', 2),
('IS Strategy', 'is402', 2),
('Web', 'is403', 2),
('Network', 'it301', 3),
('CCNA' ,'it302', 3),
('Socket ', 'it303', 3);
```



## Insert Courses With Defferent Durations
```sql
INSERT INTO Course (Duration, Sub_ID, P_id) VALUES
('3 hours', 1, 1),
('3 hours', 2, 2),
('3 hours', 3, 4),
('3 hours', 4, 3),
('3 hours', 5, 3),
('3 hours', 6, 5),
('3 hours', 7, 5),
('3 hours' ,8, 5),
('3 hours ', 9, 5);
```

## Insert data into professor
```sql
INSERT INTO Professor (Fac_id ,Dep_id , F_Name , L_Name ,Age ,Salary ,Prof_image ) 
VALUES
(1, 1, 'Mostafa', 'Kamel', 40, 8000, 'SSSSS'),
(1, 1, 'Marghany', 'Hassan', 60, 7000, 'skdsks'),
(1, 2, 'Ibrahim', 'ElAwady', 45, 1000, 'skdkskk'),
(1, 3, 'Mostafa', 'Darwish', 40, 15000, 'SSjsdSSS'),
(1, 3, 'Nagwa', 'Omar', 36, 500, 'SSSSS'),
(1, 3, 'Dalia', 'Nashaat', 30, 4500, 'hshsd'),
(1, 1, 'Mostafa', 'Hedar', 40, 12000, 'lklll'),
(1, 3, 'Ibrahim', 'Shaaban', 63, 15000, 'cnncnc'),
(1, 2, 'Mostafa', 'Abobakr', 49, 3200, 'euueu');
```

## Insert Atleast Five Students In Every Department

```sql
INSERT INTO student(F_Name, L_Name, F_Phone, Birth_date, Dep_id) 
 VALUES 
 ('Ibrahim ', 'Shaaban', '01002555227', '2002-5-9', 1),
 ('mostafa ', 'mohamed', '01096717241', '20033-1-29', 1),
 ('abdu ', 'ashraf', '01012372005', '2002-5-27', 1),
 ('mahmoud ', 'ayman', '01002445227', '2002-1-23', 1),
 ('zeyad ', 'mohamed', '01002487227', '2002-8-9', 1),
 ('noor ', 'mahmoud', '01002555276', '2001-12-3', 2),
 ('omar ', 'Ahmed', '01001235227', '2002-7-2',2),
 ('omar ', 'abdelsalam', '01004565227', '2002-9-1', 2),
 ('mohamed ', 'ammar', '01002654872', '2002-9-6', 2),
 ('ahmed ', 'hosney', '01007525227', '2002-2-4',2),
 ('mahmoud ', 'hussien', '01003452227', '2002-3-20', 3),
 ('Ali ', 'hashem', '01006595287', '2002-12-16', 3),
 ('hesham ', 'hamda', '01004590227', '2002-11-9', 3),
 ('fathy ', 'amr', '01001010127', '2002-10-19', 3),
 ('abdallah ', 'emad', '01098750565', '2002-2-15', 3);
```
	
## Insert Exams For Every Course

```sql
INSERT INTO Exams(Course_id ,examDate ,examTime , duration ) VALUES 
(2, '2023-5-29', '09:00', '2 hours'),
(3, '2023-6-3', '11:00', '2 hours'),
(4, '2023-6-7', '8:00', '2 hours'),
(5, '2023-6-11', '10:00', '2 hours'),
(6, '2023-6-15', '10:30', '2 hours'),
(7, '2023-6-17', '12:00', '2 hours'),
(8, '2023-6-19', '09:00', '2 hours'),
(9, '2023-6-22', '10:00', '2 hours');
```










 











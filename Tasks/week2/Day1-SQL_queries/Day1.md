# Exercises

## Exercise 1 - (ER diagram)
* Create ER diagram For The College Management System With following Tables
    * `Faculty` Table With These attributes:
        * `F_id:` Faculty id
        * `F_name:` Faculty Name
    * `Department` Table With These attributes:
        * `D_id:` id
        * `D_Name` Name
        * `F_id` Faculty id
    * `Address` Table With These attributes
        * `A_id` Address id
        * `Gvernorate` Gvernorate
        * `City` City
        * `line_1` Address Line 1 (Required)
        * `line_2` Address Line 2 (Optional)
    * `Student_Address` Table With These attributes
        * `Stu_A_id` id
        * `A_id` Address id
        * `Stu_id` Student id
    * `Student` Table With These attributes
        * `Stu_id` id
        * `F_Name` First Name
        * `L_Name` Last Name
        * `F_Phone` First Phone
        * `L_Phone` Last Phone
        * `Birth_Date` Birth Date
        * `image` Student Image
    * `Professor` Table With These attributes
        * `P_id` id
        * `F_id` Faculty id
        * `D_id` Department id
        * `F_name` First Name
        * `L_Name` Last Name
        * `age` Age
        * `Salary` Salary
        * `image` Student Image
    * `Subjects` Table With These attributes
        * `Sub_id` id
        * `Sub_name` Name
        * `Sub_code` Code (Unique)
        * `F_id` Faculty id
    * `Course` Table With These attributes
        * `C_id` id
        * `Sub_id` Sub_id
        * `Duration` Duration
        * `P_id` Professor id
    * `Course_Enrolment` Table With These attributes
        * `C_E_id` id
        * `C_id` Course id
        * `Stu_id` Student id
    * `Exams` Table With These attributes
        * `E_id` id
        * `C_id` Course id
        * `Date` Exam Date
        * `Time` Exam Time
        * `Duration` Exam Duration

## Exercise 2:
Convert The Above ER Diagram Into Database With Above Tables

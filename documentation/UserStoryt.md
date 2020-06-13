# User stories and database queries

### STUDENT

As a student, I can list all courses offered by the school and their details.

    SELECT Kurssi.id, Kurssi.name, Kurssi.start_date, Kurssi.end_date, Account.name 
    FROM Kurssi, Account
    WHERE Kurssi.account_id = Account.id

As a student, I can enroll in courses.

As a student, I can list all courses I have enrolled in.

    SELECT Kurssi.id, Kurssi.name, Account.name
    FROM Account, Kurssi, Enrollments
    WHERE Account.id = Enrollments.account_id
    AND Kurssi.id = Enrollments.kurssi_id
    ORDER BY Kurssi.name

As a student, I can pay for the courses I have enrolled in.

As a student, I can cancel my enrollment from a course.


### TEACHER

As a teacher, I can list all courses offered by the school and their details. (Same as above)

As a teacher, I can add new courses to the curriculum.

As a teacher, I can list the courses I am currently teaching.

    SELECT Kurssi.id, Kurssi.name, Kurssi.account_id
    FROM Kurssi
    LEFT JOIN Account ON Account_id = Account.id

As a teacher, I can list my students on all my courses.

    SELECT Account.name, Kurssi.name, Kurssi.account_id
    FROM Kurssi, Account, enrollments
    WHERE Account.id=enrollments.account_id AND Kurssi.id=enrollments.kurssi_id
    ORDER BY Kurssi.name

As a teacher, I can see all courses and number of enrollments per course.

    SELECT Kurssi.name, COUNT(Account.id)
    FROM Account, Kurssi, enrollments
    WHERE Kurssi.id=enrollments.kurssi_id AND Account.id=enrollments.account_id
    GROUP BY Kurssi.id

As a teacher, I can see how many classes each student is taking.

    SELECT Account.name, COUNT(Kurssi.id), Account.student
    FROM Account
    LEFT JOIN enrollments ON Account.id=enrollments.account_id
    LEFT JOIN Kurssi ON Kurssi.id=enrollments.kurssi_id
    GROUP BY Account.id

As a teacher, I can see who of my students have paid their invoices.



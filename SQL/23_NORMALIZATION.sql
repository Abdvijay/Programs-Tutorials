# ------------------------------ NORMALIZATION ----------------------------------------

# NOTES : 

# 1. NORMALIZATION IN SQL IS A SYSTAMATIC PROCESS OF ORGANIZING COLUMNS AND TABLES AND REDUCES THE REDUNDANCY AND IMPROVES THE INTEGRITY.
# TYPES - 1NF,2NF,3NF

# 1. 1NF - FIRST NORMAL FORM
#	     - EVERY COLUMN HOLDS ONLY ATOMIC VALUES(SINGLE VALUES) AND THAT THERE ARE NO REPEATING GROUPS.
#		 - SIMPLY SAYS THAT EACH FIELD CONTAINS SINGLE PIECE OF DATA.

Before 
-- Non-1NF Table: contains multi-valued phone_numbers in a single column
CREATE TABLE Students_Non1NF (
    student_id   INT,
    student_name VARCHAR(100),
    phone_numbers VARCHAR(100)  -- e.g., '123-4567,987-6543'
);

-- Sample data insertion (non-atomic phone numbers)
INSERT INTO Students_Non1NF (student_id, student_name, phone_numbers)
VALUES (1, 'Alice', '123-4567,987-6543'),
       (2, 'Bob', '555-1212');


After 

-- Main Students table with atomic values
CREATE TABLE Students (
    student_id   INT PRIMARY KEY,
    student_name VARCHAR(100)
);

-- Separate table for phone numbers, ensuring each phone number is atomic
CREATE TABLE StudentPhones (
    student_id INT,
    phone      VARCHAR(20),
    PRIMARY KEY (student_id, phone),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Insert students
INSERT INTO Students (student_id, student_name)
VALUES (1, 'Alice'),
       (2, 'Bob');

-- Insert phone numbers (each phone number in its own row)
INSERT INTO StudentPhones (student_id, phone)
VALUES (1, '123-4567'),
       (1, '987-6543'),
       (2, '555-1212');

# 2. 2NF - SECOND NORMAL FORM
#		 - IT REQUIRES THE TABLE SHOULD SATISFY THE 1NF.
#		 - ALL NON KEY COLUMNS FULLY FUNCTIONALLY DEPENDENT ON THE ENTIRE PRIMARY KEY.
# 		 - SIMPLY SAYS THAT TO REMOVE PARTIAL DEPENDENCY.

Before 
-- This table is in 1NF but not in 2NF because course details depend only on course_id.
CREATE TABLE Enrollment_Non2NF (
    student_id  INT,
    course_id   INT,
    course_name VARCHAR(100),
    instructor  VARCHAR(100),
    PRIMARY KEY (student_id, course_id)
);

-- Sample data insertion
INSERT INTO Enrollment_Non2NF (student_id, course_id, course_name, instructor)
VALUES (1, 101, 'Intro to SQL', 'Dr. Smith'),
       (2, 101, 'Intro to SQL', 'Dr. Smith'),
       (1, 102, 'Database Design', 'Dr. Jones');


After 

-- Table recording enrollments (relationship)
CREATE TABLE Enrollment (
    student_id INT,
    course_id  INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Table holding course details
CREATE TABLE Courses (
    course_id   INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor  VARCHAR(100)
);


-- Insert course details
INSERT INTO Courses (course_id, course_name, instructor)
VALUES (101, 'Intro to SQL', 'Dr. Smith'),
       (102, 'Database Design', 'Dr. Jones');

-- Insert enrollment data
INSERT INTO Enrollment (student_id, course_id)
VALUES (1, 101),
       (2, 101),
       (1, 102);

# 3. 3NF - THIRD NORMAL FORM
#		 - IT MUST SATISFY 2NF.
# 		 - NO TRANSITIVE DEPENDENCY.
#		 - SIMPLY SAYS THAT TO REMOVE TRANSITIVE DEPENDENCY WHERE A NON KEY COLUMN DEPENDS ON ANOTHER NON KEY COLUMN.

Before

-- This table is in 2NF but has a transitive dependency:
CREATE TABLE Courses_Non3NF (
    course_id        INT PRIMARY KEY,
    course_name      VARCHAR(100),
    instructor       VARCHAR(100),
    instructor_office VARCHAR(100)
);

-- Sample data insertion
INSERT INTO Courses_Non3NF (course_id, course_name, instructor, instructor_office)
VALUES (101, 'Intro to SQL', 'Dr. Smith', 'Room 101'),
       (102, 'Database Design', 'Dr. Jones', 'Room 102');

After 

-- Revised Courses table (now 3NF): holds course-specific data
CREATE TABLE Courses (
    course_id   INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor  VARCHAR(100),
    FOREIGN KEY (instructor) REFERENCES Instructors(instructor)
);

-- New table for instructor details
CREATE TABLE Instructors (
    instructor       VARCHAR(100) PRIMARY KEY,
    instructor_office VARCHAR(100)
);

-- Insert instructor details
INSERT INTO Instructors (instructor, instructor_office)
VALUES ('Dr. Smith', 'Room 101'),
       ('Dr. Jones', 'Room 102');

-- Insert courses with reference to instructors
INSERT INTO Courses (course_id, course_name, instructor)
VALUES (101, 'Intro to SQL', 'Dr. Smith'),
       (102, 'Database Design', 'Dr. Jones');
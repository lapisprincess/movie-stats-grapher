-- Turn on foreign keys
PRAGMA foreign_keys = ON;

-- Delete the tables if they already exist
drop table if exists Student;
drop table if exists Course;
drop table if exists Major;
drop table if exists Enroll;
drop table if exists Dept;

-- Create the schema for your tables below
CREATE TABLE Student (
	studentID INTEGER UNIQUE,
	studentName TEXT NOT NULL,
	class TEXT CHECK (
		class = 'Freshman' OR
		class = 'Sophomore' OR
		class = 'Junior' OR
		class = 'Senior'
	),
	gpa REAL CHECK (gpa >= 0.0 AND gpa <= 4.0),
	PRIMARY KEY (studentID)
);

CREATE TABLE Dept (
	deptID TEXT,
	name TEXT,
	building TEXT,
	PRIMARY KEY (deptID)
);

CREATE TABLE Major (
	studentID INTEGER REFERENCES Student(studentID), 
	major TEXT REFERENCES Dept(deptID), 
	PRIMARY KEY (studentID, major)
);

CREATE TABLE Course (
	courseNum INTEGER REFERENCES Dept(deptID),
	deptID TEXT REFERENCES Dept(deptID), 
	courseName TEXT,
	location TEXT,
	meetDay TEXT,
	meetTime TEXT CHECK (meetTime >= "07:00" AND meetTime <= "17:00"),
	PRIMARY KEY (courseNum, deptID)
);

CREATE TABLE Enroll (
	courseNum INTEGER REFERENCES Course(courseNum),
	deptID TEXT REFERENCES Course(deptID),
	studentID INTEGER REFERENCES Student(studentID),
	PRIMARY KEY (studentID)
)
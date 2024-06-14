# GPA Calculator

This project is a simple GPA calculator implemented in Python. It contains three main classes: `Course`, `Semester`, and `Student`. These classes are used to represent individual courses, group them into semesters, and calculate the GPA for each semester as well as the overall GPA for a student.

## Table of Contents
- [Usage](#usage)
- [Classes](#classes)
  - [Course](#course)
  - [Semester](#semester)
  - [Student](#student)

- [Example](#example)

## Usage

To use these classes, follow these steps:

1. Create a `Student` instance.
2. Create `Semester` instances for each semester.
3. Create `Course` instances for each course and add them to the respective semester.
4. Calculate the GPA for each semester.
5. Add the semesters to the student.
6. Calculate the total GPA for the student.

## Classes

### Course

Represents a course taken by a student.

#### Methods

- `__init__(self, ClassName, credits, grade, semester)`: Initializes a course instance.
  - **ClassName**: The name of the course (e.g., 'CS115').
  - **credits**: The number of credits the course is worth.
  - **grade**: The grade received in the course (A, B, C, D).
  - **semester**: The semester instance to which this course belongs.

### Semester

Represents a semester containing multiple courses.

#### Methods

- `__init__(self, season, year)`: Initializes a semester instance.
  - **season**: The season of the semester (e.g., 'fall', 'spring').
  - **year**: The year of the semester.
  
- `addCourses(self, course)`: Adds a course to the semester.
  - **course**: The course instance to be added.
  
- `gpa(self)`: Calculates and prints the GPA for the semester.

### Student

Represents a student with multiple semesters.

#### Methods

- `__init__(self, name)`: Initializes a student instance.
  - **name**: The name of the student.
  
- `addSemesters(self, semester)`: Adds a semester to the student's record.
  - **semester**: The semester instance to be added.
  
- `totalGPA(self)`: Calculates and prints the total GPA for the student across all semesters.



## Example

```python
# Create a student instance
Student1 = Student('Malachi Rosario')

# Create semester instances
Semester1 = Semester('fall', 2022)
Semester2 = Semester('spring', 2023)
Semester3 = Semester('fall', 2023)
Semester4 = Semester('spring', 2024)

# Add courses to semesters
course1 = Course('cs115', 2, 'B', Semester1)
course2 = Course('cs100', 2, 'B', Semester1)
course3 = Course('MATH152', 5, 'C', Semester1)
course4 = Course('ds151', 3, 'D', Semester1)

course5 = Course('Hum200', 3, 'A', Semester2)
course6 = Course('cs116', 2, 'A', Semester2)
course7 = Course('MATH251', 4, 'B', Semester2)
course8 = Course('Phsyc123', 4, 'B', Semester2)
course9 = Course('ECON211', 3, 'B', Semester2)

course10 = Course('cs331', 3, 'A', Semester3)
course11 = Course('cs330', 3, 'B', Semester3)
course12 = Course('MATH332', 3, 'A', Semester3)
course13 = Course('Phyc301', 3, 'A', Semester3)
course14 = Course('FDNS304', 3, 'A', Semester3)

course15 = Course('MATH474', 3, 'A', Semester4)
course16 = Course('CS350', 3, 'B', Semester4)
course17 = Course('CS425', 3, 'B', Semester4)
course18 = Course('Phycs221', 4, 'B', Semester4)
course19 = Course('PS338', 3, 'B', Semester4)

# Calculate GPA for each semester
Semester1.gpa()
Semester2.gpa()
Semester3.gpa()
Semester4.gpa()

# Add semesters to student
Student1.addSemesters(Semester1)
Student1.addSemesters(Semester2)
Student1.addSemesters(Semester3)
Student1.addSemesters(Semester4)

# Calculate total GPA for student
Student1.totalGPA()

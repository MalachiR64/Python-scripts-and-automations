# Python Automation Scripts

This repository contains a collection of Python scripts for various automation tasks. Below is a table of contents linking to each script's directory.

## Table of Contents
- Scripts
    - [Website Blocker](./WebsiteBlocker)
    - [College GPA Calculator](./CollegeGPACalculator)

## Scripts

## [Website Blocker](./WebsiteBlocker)

A Python script to block access to specified websites on Windows and Mac devices by modifying the host file to redirect the websites to the local loopback address (127.0.0.1).



### Usage

1. **Define Websites to Block:** Open the script and modify the `site_to_block` list with the websites you want to block.
    ```python
    site_to_block = ['www.example.com', 'example.com']
    ```
2. **Specify Host File Path:**
    - For MacOS:
      ```python
      hostPathM = r"/etc/hosts"
      ```
    - For Windows:
      ```python
      hostPathW = r"C:\Windows\System32\drivers\etc\hosts"
      ```
3. **Run the Script:** The script will block the specified websites if the current date is before the `endTime` variable. It will relaunch itself with administrative privileges if not already running as an administrator.

## [College GPA Calculator](./CollegeGpaCalculator)

This script helps manage courses, semesters, and students, including calculating the GPA for each semester and the overall GPA for a student.

### Classes and Methods

1. **Course Class:**
   - Attributes: `ClassName`, `credits`, `grade`, `semester`
   - Initializes the course and adds it to the specified semester.

2. **Semester Class:**
   - Attributes: `season`, `year`
   - Methods: `addCourses(course)`, `gpa()`
   - Manages courses within a semester and calculates the semester GPA.

3. **Student Class:**
   - Attributes: `name`
   - Methods: `addSemesters(semester)`, `totalGPA()`
   - Manages the student's semesters and calculates the overall GPA.

### Example

```python
# Create a semester
fall2023 = Semester('Fall', 2023)

# Add courses to the semester
course1 = Course('Math101', 3, 'A', fall2023)
course2 = Course('History202', 4, 'B', fall2023)

# Calculate semester GPA
fall2023.gpa()

# Create a student and add the semester
student = Student('John Doe')
student.addSemesters(fall2023)

# Calculate total GPA for the student
student.totalGPA()

class Course:
    def __init__(self, ClassName, credits, grade, semester):
        self.ClassName = ClassName
        self.credits = credits
        self.grade = grade
        self.semester = semester

        for i, char in enumerate(self.ClassName):
            if char.isnumeric():
                self.DepartmentName = self.ClassName[:i]
                self.CourseNumber = self.ClassName[i:]
                break
        semester.addCourses(self)
        print("coursename:", self.DepartmentName, "CourseNumber:", self.CourseNumber, 'credits:', self.credits, 'grade:', self.grade, 'semester:', self.semester.semesterName )


class Semester:
    def __init__(self, season, year):
        self.season = season
        self.year = year
        self.courses = []
        self.semesterName= f'season: {self.season}, year: {self.year}'
        print(self.semesterName)
    def addCourses(self, course):
        self.courses.append(course)

    def gpa(self):
        self.semestertotalCredits = 0
        self.semestertotalPoints = 0
        self.semestertotalsemesterGpa = 0
        for i in self.courses:
            coursePoints = 0
            if i.grade == 'A':
                coursePoints = 4
            elif i.grade == 'B':
                coursePoints = 3
            elif i.grade == 'C':
                coursePoints = 2
            elif i.grade == 'D':
                coursePoints = 1
            self.semestertotalPoints += coursePoints * i.credits
            self.semestertotalCredits += i.credits
        SemesterGPA = self.semestertotalPoints / self.semestertotalCredits
        print( 'semester:',self.semesterName, 'semester gpa:', SemesterGPA,'\n')

class Student:
    def __init__(self, name) :
        self.name = name
        self.totalCredits = 0
        self.totalPoints = 0
        self.Semesters = []
    def addSemesters(self,semester): 
        self.Semesters.append(semester)
    def totalGPA (self):
        for i in self.Semesters:
            self.totalCredits += i.semestertotalCredits
            self.totalPoints += i.semestertotalPoints
        self.gpa = self.totalPoints / self.totalCredits
        print('student name', self.name, 'gpa', self.gpa, )

 

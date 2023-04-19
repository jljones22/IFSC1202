class Student:
    def __init__(self, firstName, lastName, tNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.tNumber = tNumber
        self.courseList = []

class StudentList:
    def __init__(self):
        self.studentList = []
    
    def addStudent(self, firstName, lastName, tNumber):
        self.studentList.append(Student(firstName, lastName, tNumber))

    def findStudent(self, studentToFind):
        for i in range(len(self.studentList)):
            if self.studentList[i].tNumber == studentToFind: return i
        else: return -1

    def printStudent(self):
        print(f"{'First Name':<19}{'Last Name':<19}{'T-Number':<19}{'Course':<19}{'Name':<50}{'Room':<14}{'Meeting Times':<13}")
        
        for i in range(len(self.studentList)):
            print(f"{self.studentList[i].firstName:<19}{self.studentList[i].lastName:<19}{self.studentList[i].tNumber}{'':<19}{'':<50}{'':<14}{'':<13}")
            for j in range(len(self.studentList[i].courseList)):
                print(f"{'':<19}{'':<19}{'':<19}{self.studentList[i].courseList[j].department:<19}{self.studentList[i].courseList[j].name:<50}{self.studentList[i].courseList[j].room:<14}{self.studentList[i].courseList[j].meetingTimes:<13}")


    def addStudentFromFile(self, filename):
        students = open(filename, "rt")
        line = students.readline()

        while line != "":
            ls = line.strip().split(',')
            self.addStudent(ls[0], ls[1], ls[2])
            line = students.readline()
        students.close()

class Course:
    def __init__(self, department, number, name, room, meetingTimes):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingTimes = meetingTimes

class CourseList:
    def __init__(self):
        self.courseList = []

    def addCourse(self, department, number, name, room, meetingTimes):
        self.courseList.append(Course(department, number, name, room, meetingTimes))

    def findCourse(self, departmentToFind, numberToFind):
        for i in range(len(self.courseList)):
            if self.courseList[i].department == departmentToFind and self.courseList[i].number == numberToFind:
                return i
        else: return -1

    def addCourseFromFile(self, filename):
        courses = open(filename, "rt")
        line = courses.readline()

        while line != "":
            ls = line.strip().split(',')
            self.addCourse(ls[0], ls[1], ls[2], ls[3], ls[4])
            line = courses.readline()
        courses.close()


CourseList = CourseList()
CourseList.addCourseFromFile("11.03 Courses.txt")

StudentList = StudentList()
StudentList.addStudentFromFile("11.03 Students.txt")

Registration = open("11.03 Registration.txt")
line = Registration.readline()

while line != "":
    ls = line.strip().split(',')

    indexC = CourseList.findCourse(ls[1], ls[2])

    indexS = StudentList.findStudent(ls[0])

    StudentList.studentList[indexS].courseList.append(Course(CourseList.courseList[indexC].department, CourseList.courseList[indexC].number, CourseList.courseList[indexC].name, CourseList.courseList[indexC].room, CourseList.courseList[indexC].meetingTimes))
    line = Registration.readline()
    
StudentList.printStudent()
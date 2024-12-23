class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def input():
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        return Student(student_id, name, dob)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.marks = {}

    def input():
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        return Course(course_id, name)

    def input_marks(self, students):
        print(f"\nInput marks for course: {self.name}")
        for student in students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            self.marks[student.id] = mark

    def show_marks(self, students):
        print(f"\nMarks for course: {self.name}")
        for student in students:
            if student.id in self.marks:
                print(f"{student.name} (ID: {student.id}): {self.marks[student.id]}")
            else:
                print(f"{student.name} (ID: {student.id}): No mark available")

    def __str__(self):
        return f"Course: {self.name}, ID: {self.id}"

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            print(f"\nInput information for student {i + 1}:")
            self.students.append(Student.input())
        self.save_data()

    def input_courses(self):
        num_courses = int(input("\nEnter the number of courses: "))
        for i in range(num_courses):
            print(f"\nInput information for course {i + 1}:")
            self.courses.append(Course.input())
        self.save_data()

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def input_marks(self):
        self.list_courses()
        course_id = input("\nEnter the course ID to input marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            course.input_marks(self.students)
            self.save_data()
        else:
            print("Invalid course ID.")

    def show_marks(self):
        self.list_courses()
        course_id = input("\nEnter the course ID to show marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            course.show_marks(self.students)
        else:
            print("Invalid course ID.")

    def save_data(self):
        with open("student_mark.txt", "w") as file:
            file.write("Students:\n")
            for student in self.students:
                file.write(f"{student}\n")
            file.write("\nCourses:\n")
            for course in self.courses:
                file.write(f"{course}\n")
                file.write("Marks:\n")
                for student_id, mark in course.marks.items():
                    file.write(f"  Student ID: {student_id}, Mark: {mark}\n")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. List courses")
            print("2. List students")
            print("3. Input marks for a course")
            print("4. Show student marks for a course")
            print("5. Exit")
            choice = int(input("Select an option: "))

            if choice == 1:
                self.list_courses()
            elif choice == 2:
                self.list_students()
            elif choice == 3:
                self.input_marks()
            elif choice == 4:
                self.show_marks()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = StudentMarkManagement()
    app.input_students()
    app.input_courses()
    app.run()

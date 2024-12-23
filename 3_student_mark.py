import os
import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    @staticmethod
    def input():
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        return Student(student_id, name, dob)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id}, DoB: {self.dob}, GPA: {self.gpa:.1f}"

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits
        self.marks = {}

    @staticmethod
    def input():
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        credits = int(input("Enter Course Credits: "))
        return Course(course_id, name, credits)

    def input_marks(self, students):
        print(f"\nInput marks for course: {self.name}")
        for student in students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            self.marks[student.id] = math.floor(mark * 10) / 10  # Round down to 1 decimal

    def show_marks(self, students):
        print(f"\nMarks for course: {self.name}")
        for student in students:
            if student.id in self.marks:
                print(f"{student.name} (ID: {student.id}): {self.marks[student.id]}")
            else:
                print(f"{student.name} (ID: {student.id}): No mark available")

    def __str__(self):
        return f"Course: {self.name}, ID: {self.id}, Credits: {self.credits}"

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.load_data()

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

    def calculate_gpa(self):
        for student in self.students:
            total_credits = 0
            weighted_sum = 0
            for course in self.courses:
                if student.id in course.marks:
                    weighted_sum += course.marks[student.id] * course.credits
                    total_credits += course.credits
            student.gpa = (weighted_sum / total_credits) if total_credits > 0 else 0
        self.save_data()

    def sort_students_by_gpa(self):
        self.calculate_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        print("\nStudents sorted by GPA:")
        self.list_students()

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

    def load_data(self):
        if not os.path.exists("student_mark.txt"):
            return
        with open("student_mark.txt", "r") as file:
            lines = file.readlines()

        mode = None
        for line in lines:
            line = line.strip()
            if line == "Students:":
                mode = "students"
            elif line == "Courses:":
                mode = "courses"
            elif mode == "students" and line:
                parts = line.split(", ")
                student_id = parts[1].split(": ")[1]
                name = parts[0].split(": ")[1]
                dob = parts[2].split(": ")[1]
                gpa = float(parts[3].split(": ")[1])
                student = Student(student_id, name, dob)
                student.gpa = gpa
                self.students.append(student)
            elif mode == "courses" and line and not line.startswith("Marks:"):
                parts = line.split(", ")
                course_id = parts[1].split(": ")[1]
                name = parts[0].split(": ")[1]
                credits = int(parts[2].split(": ")[1])
                self.courses.append(Course(course_id, name, credits))
            elif line.startswith("  Student ID:"):
                student_id = line.split(", ")[0].split(": ")[1]
                mark = float(line.split(", ")[1].split(": ")[1])
                self.courses[-1].marks[student_id] = mark

    def decorate_ui(self):
        def draw_menu(stdscr):
            curses.start_color()
            curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
            stdscr.clear()
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(0, 0, "Welcome to the Student Mark Management System")
            stdscr.attroff(curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
        curses.wrapper(draw_menu)

    def run(self):
        self.decorate_ui()
        while True:
            print("\nMenu:")
            print("1. List courses")
            print("2. List students")
            print("3. Input marks for a course")
            print("4. Show student marks for a course")
            print("5. Calculate GPA")
            print("6. Sort students by GPA")
            print("7. Exit")
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
                self.calculate_gpa()
            elif choice == 6:
                self.sort_students_by_gpa()
            elif choice == 7:
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()

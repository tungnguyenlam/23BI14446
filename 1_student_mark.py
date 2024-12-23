def inputStudentInfo():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    student_dob = input("Enter Student Date of Birth: ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def inputCourseInfo():
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    return {"id": course_id, "name": course_name}

def listStudents(student_list):
    print("\nList of Students:")
    for student in student_list:
        print(f"Student: {student['name']}, ID: {student['id']}, DoB: {student['dob']}")

def listCourses(course_list):
    print("\nList of Courses:")
    for course in course_list:
        print(f"Course: {course['name']}, ID: {course['id']}")

def inputMarks(student_list, course, marks):
    print(f"\nInput marks for course: {course['name']}")
    for student in student_list:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[course['id']][student['id']] = mark

def showMarks(course, student_list, marks):
    print(f"\nMarks for course: {course['name']}")
    for student in student_list:
        student_id = student['id']
        if student_id in marks[course['id']]:
            print(f"{student['name']} (ID: {student_id}): {marks[course['id']][student_id]}")
        else:
            print(f"{student['name']} (ID: {student_id}): No mark available")

def main():
    student_list = []
    course_list = []
    marks = {}

    # Input number of students and their information
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print(f"\nInput information for student {i + 1}:")
        student_list.append(inputStudentInfo())

    # Input number of courses and their information
    num_courses = int(input("\nEnter the number of courses: "))
    for i in range(num_courses):
        print(f"\nInput information for course {i + 1}:")
        course = inputCourseInfo()
        course_list.append(course)
        marks[course['id']] = {}

    while True:
        print("\nMenu:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = int(input("Select an option: "))

        if choice == 1:
            listCourses(course_list)
        elif choice == 2:
            listStudents(student_list)
        elif choice == 3:
            listCourses(course_list)
            course_id = input("\nEnter the course ID to input marks: ")
            selected_course = next((course for course in course_list if course['id'] == course_id), None)
            if selected_course:
                inputMarks(student_list, selected_course, marks)
            else:
                print("Invalid course ID.")
        elif choice == 4:
            listCourses(course_list)
            course_id = input("\nEnter the course ID to show marks: ")
            selected_course = next((course for course in course_list if course['id'] == course_id), None)
            if selected_course:
                showMarks(selected_course, student_list, marks)
            else:
                print("Invalid course ID.")
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

main()

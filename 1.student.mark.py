def inputStudentInfo():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    student_dob = input("Enter Student Date of Birth: ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def listStudent(student_dic):
    len_list = len(student_dic)
    for i in range(len_list):
        print(f"Student: {student_dic[i]['name']}, ID: {student_dic[i]['id']}, DoB: {student_dic[i]['dob']}")

while True:
    num_student = int(input("Input the number of student"))
    student_dic = []
    for i in range(num_student):
        print("Input student ", i, "th")
        student_dic.append(inputStudentInfo())

    print("1.List course \n2.List students \n3.Show student mark \n4.")
    mode = int(input("Go to"))
    if mode == 1:
        listCourse()
    elif mode == 2:
        listStudent()
    elif mode == 3:
        break
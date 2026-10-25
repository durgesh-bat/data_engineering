import json
student = {
    "id": 101,
    "name": "Amit",
    "age": 21,
    "course": "BCA",
    "marks": 52
}


def test():
    # Python → JSON string
    student = json.dumps(student)
    print("Type of Student: ",type(student))
    print(student)

    # JSON string → Python
    student=json.loads(student)
    print(student)
    print(type(student))

def Test_writen():
    with open("Data/student.json",'w') as file:
        json.dump(student,file,indent=4)

# Test_writen()

def Test_reading():
    with open("Data/student.json",'r') as file:
        student_data = json.load(file)
        print(student_data)
        print(type(student_data))
# Test_reading()

# -----------------Task 1 -------------------

def Task1():
    with open('Data/student.json','r') as file:
        student_data = json.load(file)
        return student_data

# -----------------Task 2 -------------------

def Task2():
    with open('Data/student.json','r') as file:
        students = json.load(file)
        for item in students:
            print(f"{item['name']} -> {item['contact']['city']}-> {item['marks']}")

# Task2()
# -----------------Task 3 -------------------

def Task3():
    with open('Data/student.json','r') as file:
        students = json.load(file)
        highest_mark_student={}
        mark=0
        for item in students:
            if item['marks']>mark:
                mark = item['marks']
                highest_mark_student = item
        return highest_mark_student

# print("Highest Marks: ",Task3())

# -----------------Task 4 -------------------

def Task4():
    with open('Data/student.json','r') as file:
        students = json.load(file)
        total=0
        count=0
        for item in students:
            total+=item['marks']
            count+=1
    return total/count

# print("Average of Marks: ",Task4())

# -----------------Task 5 -------------------

def Task5():
    with open('Data/student.json','r') as file:
        students = json.load(file)
        students_60_pluse=[]
        for item in students:
            if item['marks']>=60:
                students_60_pluse.append(item)
    return students_60_pluse

# print('60 Plus student marks: ',Task5())

# -----------------Task 6 -------------------

def Task6():
    with open('Data/student.json','r') as file:
        students = json.load(file)
        student_list=[]
        for item in students:
            temp={
                "name":item['name'],
                "city":item['contact']['city'],
                "marks":item['marks']
            }
            student_list.append(temp)
        return student_list

# print(Task6())

# -----------------Task 7 -------------------

def Task7():
    student_list=[]
    with open('Data/student.json','r') as file:
        students = json.load(file)
        for item in students:
            temp={
                "name":item['name'],
                "city":item['contact']['city'],
                "marks":item['marks']
            }
            student_list.append(temp)
    with open('Data/student_summary.json','w') as file:
        json.dump(student_list,file,indent=4)      
Task7()
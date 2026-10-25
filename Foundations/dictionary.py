students = [
    {
        "id": 101,
        "name": "Amit",
        "age": 21,
        "course":"BCA",
        "marks":52
    },
    {
        "id": 102,
        "name": "Rahul",
        "age": 22,
        "course":"B.Tech",
        "marks":65
    },
    {
        "id": 103,
        "name": "Priya",
        "age": 20,
        "course":"BBA",
        "marks":57
    },
    {
        "id":104,
        "name":"Ramesh",
        "age":25,
        "course":"MCA",
        "marks":70
    },
    {
        "id":105,
        "name":"Raju",
        "age":26,
        "course":"MBA",
        "marks":69
    }
]

# # Task 1
# print("---------Task 1 ----------")
# for student in students:
#     print(student['name'])

# # Task 2
# print("---------Task 2 -----------")
# for student in students:
#     print(f"{student["name"]} | {student['marks']}")

# # Task 3
# print("---------Task 3 -----------")
# highest_marks = students[0]

# for student in students:
#     if student["marks"] > highest_marks['marks']:
#         highest_marks= student

# print(f"Highest Student: {highest_marks['name']}")
# print(f"Highest marks: {highest_marks['marks']}")

# # Task 4 
# print("--------Task 4 -----------")
# list_marks=[]
# for student in students:
#     list_marks.append(student["marks"])
# print("Average Students Marks: ", sum(list_marks)/len(list_marks))

# # Task 5 
# print("--------------Task 5 ------------")

# for student in students:
#     if student["marks"]>=60:
#         print("Student marks: ",student["marks"])
    
def find_top_student(students):
    top_student = students[0]
    for student in students:
        if student["marks"] > top_student['marks']:
            top_student= student
    return top_student

def calculate_average(students):
    list_marks=[]
    for student in students:
        list_marks.append(student["marks"])
    return sum(list_marks)/len(list_marks)


def get_passed_students(students):
    pass_students=[]
    for student in students:
        if student["marks"]>=60:
            pass_students.append(student)
    return pass_students

top_student = find_top_student(students)
average = calculate_average(students)
passed_students = get_passed_students(students)

print("Top Stduent:",top_student)
print("Average",average)
print("Pass Students",passed_students)
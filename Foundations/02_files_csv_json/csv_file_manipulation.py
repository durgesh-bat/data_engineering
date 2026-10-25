import csv

# with open("Data/Students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     print(reader)
#     for row in reader:
#         print(row)



#------------- Task 1 ----------------
def read_CSV():
    with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


# ------------Task 2 ----------------
def PrintCSV_Format():
    with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']} -> {row['course']} -> {row['marks']}")
            # print(row[0])

# PrintCSV_Format()

# ------------Task 3-----------------

def Highest_marks_CSV():
     with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        highest_student={"marks":0}
        for item in reader:
            if int(item['marks'])>int(highest_student['marks']):
                highest_student=item
        return highest_student
# Highest_marks_CSV()
#-------------Task 4 -----------------
def Avg_CSV():
    with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        avg={"sum":0,"count":0,"avg":0}
        for item in reader:
            avg['sum']+=int(item['marks'])
            avg['count']+=1
        avg['avg']=avg['sum']/avg['count']
        return avg['avg']

# Avg_CSV()

# - ------------ Task 5 -------------
def passed_CSV():
    with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        pass_students=[]
        for item in reader:
            if int(item['marks'])>=60:
                pass_students.append(item)
        return pass_students

# print(passed_CSV())

# ---------------- Task 6 -----------

def ETL_style_CSV():
    with open("Data/Students.csv", "r") as file:
        reader = csv.DictReader(file)
        pass_students=[]
        for item in reader:
            if int(item['marks'])>=60:
                pass_students.append(item)
        print(pass_students)
    with open("Data/passed_students.csv", "w",newline="") as file:
        fieldnames = ["id", "name", "age", "course", "marks"]
        writer = csv.DictWriter(file,fieldnames)
        writer.writeheader()
        writer.writerows(pass_students)

ETL_style_CSV()


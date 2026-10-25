import csv

def ReadCSV():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            print(item)

# -------------- Task 2 ---------------
def ConvertInt():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            try:
                mark = int(item['marks'])
            except ValueError:
                print("invailid marks")
                continue

# ConvertInt()

# ReadCSV()
# -------------- Task 3 ---------------

def MarksInvailid():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            try:
                mark = int(item['marks'])
            except ValueError:
                print("Invailid marks for ",item['name'])
                continue

# MarksInvailid()

# -------------- Task 4 ---------------

def AverageCSV():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        count = 0
        total = 0
        for item in reader:
            try:
                total+=int(item['marks'])
                count+=1
            except ValueError:
                print("Invailid marks for ",item['name'])
                continue
        print(f"avg:{total}/{count}={total/count}")
        return total/count

# -------------- Task 5 ---------------


def Passed_students():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        pass_students=[]
        for item in reader:
            try:
                if int(item['marks'])>=60:
                    pass_students.append(item)
            except ValueError:
                continue
        return pass_students
    
print(Passed_students())

# -------------- Task 6 ---------------

def invalid_students():
    with open('Data/Students_dirty.csv','r') as file:
        reader = csv.DictReader(file)
        invalid_students_list=[]
        for item in reader:
            try:
                int(item['marks'])
            except ValueError:
                invalid_students_list.append(item)
    with open('Data/invalid_students.csv','w') as file:
        fieldsname=['id','name','age','course','marks']
        writer = csv.DictWriter(file,fieldnames=fieldsname)       
        
        writer.writeheader()
        writer.writerows(invalid_students_list)

invalid_students()
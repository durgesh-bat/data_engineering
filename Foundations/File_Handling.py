# Read file

# with open("students.txt",'r') as file:
#     for line in file:
#         print(line.strip())

# Write using W

# with open("output.txt",'w') as file:
#     file.write("Learning of Data Engineering")

# with open("output.txt",'r') as file:
#     print(file.read())

# Append in file using a

# with open("students.txt", "w") as file:
#     file.write("""Amit,52
# Rahul,65
# Priya,57
# Ramesh,70
# Raju,69""")

# Task 1

def readfile(filename):
    with open(filename,'r') as file:
        print(file.read())

def readbyline(filename):
    with open(filename,'r') as file:
        for line in file:
            print(line.strip())

def topStudents(filename):
    with open(filename, "r") as file:
        for line in file:
            name, marks = line.strip().split(",")

            if int(marks) >= 60:
                print(f"{name} → {marks}")

def avgmarks(filename):
    total = 0
    count = 0

    with open(filename, "r") as file:
        for line in file:
            name, marks = line.strip().split(",")

            total += int(marks)
            count += 1

    print("Average:", total / count)

def newData(filename):
    data="""
            Rahul,65
            Ramesh,70
            Raju,69
        """
    with open(filename,'w') as file:
        file.write(data)
    with open(filename,'r') as file:
        print(file.read())

newData("newfile.txt")
avgmarks("students.txt")
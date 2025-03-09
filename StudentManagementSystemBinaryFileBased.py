# BINARY FILE BASED STUDENT MANAGEMENT SYSTEM PROJECT

# Importing Required Libararies
import pickle
import os

# A Method to add a student
def addStudent():
    file = open('student.dat','ab')
    roll = input("\n\tEnter Roll Number : ")
    name = input("\tEnter Student Name : ")
    add = input("\tEnter Student Address : ")
    mob = input("\tEnter Student Mobile : ")
    pickle.dump(roll,file)
    pickle.dump(name,file)
    pickle.dump(add,file)
    pickle.dump(mob,file)
    pickle.dump('0',file)
    pickle.dump('0',file)
    pickle.dump('0',file)
    pickle.dump('0',file)
    print("\n\tStudent Added Successfully!")
    input("\n\tPress Enter To Continue...")
    file.close()

# A Method to view all student's details
def viewAllStudent():
    file = open('student.dat','rb')
    print("\n\nRollNo\tName\tAddres\tMobile\tMath\tSci\tEng\tHin\n")
    try:
        while True :
            data = pickle.load(file)
            print(data,end="\t")
    except EOFError as e:
        print("\n\n\tAll Students Information Loaded")
    file.close()
    input("\n\tPress Enter To Continue...")

# A Method to update marks of a student
def updateMarks():
    file1 = open('student.dat','rb')
    file2 = open('temp.dat','ab')
    flag = 0
    try:
        roll = input("\n\tEnter Student Roll Number : ")
        while True:
            data = pickle.load(file1)
            if(data == roll):
                flag = 1
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                math = input("\n\tEnter Math Marks : ")
                sci = input("\tEnter Science Marks : ")
                eng = input("\tEnter English Marks : ")
                hin = input("\tEnter Hindi Marks : ")
                pickle.dump(math,file2)
                pickle.dump(sci,file2)
                pickle.dump(eng,file2)
                pickle.dump(hin,file2)
            else:
                pickle.dump(data,file2)
    except:
        if(flag==1):
            print('\n\tStudent Record Updated Successfully!')
        else:
            print("\n\tStudent Not Found on This Roll Number!")
    file1.close()
    file2.close()
    os.remove('student.dat')
    os.rename('temp.dat','student.dat')
    input("\n\tPress Enter To Continue...")

# A Method to delete a Student
def deleteStudent():
    file1 = open('student.dat','rb')
    file2 = open('temp.dat','ab')
    flag = 0
    roll = input("\n\tEnter Student Roll No To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if(data == roll):
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if(flag==1):
            print("\n\tStudent Deleted Successfully!")
        else:
            print("\n\tStudent Not Found On This Roll No!")
    file1.close()
    file2.close()
    os.remove('student.dat')
    os.rename('temp.dat','student.dat')
    input("\n\tPress Enter To Continue...")

# A Method to Update A Student
def updateStudent():
    file1 = open('student.dat','rb')
    file2 = open('temp.dat','ab')
    flag = 0
    roll = input("\n\tEnter Roll Number To Update Student Info : ")
    try:
        while True:
            data = pickle.load(file1)
            if(data == roll):
                flag = 1
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.load(file1)
                pickle.load(file1)
                add = input("\n\tEnter New Address : ")
                mob = input("\tEnter New Mobile Number : ")
                pickle.dump(add,file2)
                pickle.dump(mob,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\tStudent Info Updated Successfully!")
        else:
            print("\n\tStudent Not Found On This Roll No!")
    file1.close()
    file2.close()
    os.remove('student.dat')
    os.rename('temp.dat','student.dat')
    input("\n\tPress Enter To Continue...")

# Dashboard
while True:
    print("\n\t***** STUDENT MANAGEMENT SYSTEM *****")
    print("\n\t1. Add Student")
    print("\t2. Update Marks")
    print("\t3. View All Students")
    print("\t4. Delete A Student")
    print("\t5. Update A Student")
    print("\t6. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if(ch==6):
        print("\n\t--- Bye-Bye Admin!")
        break
    elif ch==1:
        addStudent()
    elif ch==2:
        updateMarks()
    elif ch==3:
        viewAllStudent()
    elif ch==4:
        deleteStudent()
    elif ch==5:
        updateStudent()
    else:
        input("\n\tWrong Choice...\n\tTry Again...\n")

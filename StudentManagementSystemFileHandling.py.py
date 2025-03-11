# SCHOOL MANAGEMENT SYSTEM

# IMPORTING REQUIRED LIBRARIES
import pickle
import os

# A Method to Add A Student In File.
def addStudent():
    file = open('student.dat','ab')
    roll = input("\n\tEnter Student Roll Number : ")
    name = input("\tEnter Student Name : ")
    course = input("\tEnter Student Course : ")
    add = input("\tEnter Student Address : ")
    mob = input("\tEnter Student Mobile Number : ")
    pickle.dump(roll,file)
    pickle.dump(name,file)
    pickle.dump(course,file)
    pickle.dump(add,file)
    pickle.dump(mob,file)
    print("\n\tStudent Added Successfully!")
    file.close()
    input("\n\tPress Enter To Continue...")

# A Method to Find A Student From A File.
def findStudent():
    file = open('student.dat','rb')
    flag = 0
    roll = input("\n\tEnter Roll Number To Find Student : ")
    try:
        while True:
            data = pickle.load(file)
            if( data == roll ):
                print("\n\tStudent Name :",pickle.load(file))
                print("\tStudent Course Name :",pickle.load(file))
                print("\tStudent Address :",pickle.load(file))
                print("\tStudent Mobile Number :",pickle.load(file))
                flag = 1
    except:
        if flag==0:
            print("\n\tStudent Not Found On This Roll Number!")
    file.close()
    input("\n\tPress Enter To Continue...")

# A Method to Count All The Students From File
def countStudent():
    file = open('student.dat','rb')
    count = 0
    try:
        while True:
            data = pickle.load(file)
            count=count+1
    except:
        print("\n\tTotal Number Of Students Are : ",int(count/5))
    file.close()
    input("\n\tPress Enter To Continue...")

# A Method To Delete A Student From File.
def deleteStudent():
    file1 = open('student.dat','rb')
    file2 = open('temp.dat','ab')
    flag = 0
    try:
        roll = input("\n\tEnter Roll Number To Delete A Student : ")
        while True:
            data = pickle.load(file1)
            if data == roll:
                print("\n\tStudent Name : ",pickle.load(file1))
                print("\tStudent Course  : ",pickle.load(file1))
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
                print("\n\tStudent Deleted Successfully!")
            else:
                pickle.dump(data,file2)
    except:
        if flag==0:
            print("\n\tStudent Not Found On This Roll Number!")
    file1.close()
    file2.close()
    os.remove('student.dat')
    os.rename('temp.dat','student.dat')
    input("\n\tPress Enter To Continue...")

# A Method to Update A Student In File.
def updateStudent():
    file1 = open('student.dat','rb')
    file2 = open('temp.dat','ab')
    flag = 0
    roll = input("\n\tEnter Roll Number To Update A Student  : ")
    try:
        while True:
            data = pickle.load(file1)
            if data == roll:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.load(file1)
                pickle.load(file1)
                add = input("\n\tEnter New Address : ")
                mob = input("\tEnter New Mobile Number : ")
                pickle.dump(add,file2)
                pickle.dump(mob,file2)
                flag = 1
                print("\n\tStudent Updated Successfully!")
            else:
                pickle.dump(data,file2)
    except:
        if flag==0:
            print("\n\tStudent Not Found!")
    file1.close()
    file2.close()
    os.remove('student.dat')
    os.rename('temp.dat','student.dat')
    input("\n\tPress Enter To Continue...")

# DASHBOARD
while True:
    print("\n\t***** STUDENT MANAGEMENT SYSTEM ***** ")
    print("\n\t1. Add Student")
    print("\t2. Find Student")
    print("\t3. Count Student")
    print("\t4. Delete A Student")
    print("\t5. Update A Student")
    print("\t6. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if ch==6:
        print("\n\t--- Bye-Bye Admin!")
        break
    elif ch==1:
        addStudent()
    elif ch==2:
        findStudent()
    elif ch==3:
        countStudent()
    elif ch==4:
        deleteStudent()
    elif ch==5:
        updateStudent()
    else:
        input("\n\tWrong Entered\n\tTry Again!")

# EMPLOYEE MANAGEMENT SYSTEM


import pickle
import os
# FUNCTION TO ADD AN EMPLOYEE
def addEmp():
    file = open("emp.dat","ab")
    choice = "Y"
    while(choice in "Yy"):
        empid = input("\nEnter New Employee ID : ")
        name = input("Enter Employee Name : ")
        add = input("Enter Employee Address : ")
        sal = input("Enter Employee Salary : ")
        pickle.dump(empid,file)
        pickle.dump(name,file)
        pickle.dump(add,file)
        pickle.dump(sal,file)
        print("\nEmployee Added Successfully!\n")
        choice = input("Do You Want To Add One More Employee (Y/N) : ")
    file.close()


# FUNCTION TO VIEW ALL EMPLOYEES
def viewAllEmp():
    file = open("emp.dat","rb")
    try:
        while(True):
            print("Employee ID : ",pickle.load(file))
            print("Employee Name : ",pickle.load(file))
            print("Employee Address : ",pickle.load(file))
            print("Employee Salary : ",pickle.load(file),"\n")
    except EOFError as e:
        print("\n All Employee Data Loaded Successfully!")
        input()
    file.close()


# FUNCTION TO VIEW AN EMPLOYEE BY ID
def viewById():
    file = open("emp.dat","rb")
    empid = input("\nEnter Employee ID : ")
    try:
        while(True):
            ids = pickle.load(file)
            if(ids==empid):
                print("Employee Name :",pickle.load(file))
                print("Employee Address :",pickle.load(file))
                print("Employee Salary :",pickle.load(file))
                file.close()
                input()
                break
    except EOFError as e:
        print("\nEmployee Not Found!\n")
        input()
    file.close()

# FUNCTION TO DELETE AN EMPLOYEE
def delEmp():
    file = open("emp.dat","rb")
    tempFile = open("temp.dat","ab")
    empid = input("Enter Employee ID To Delete : ")
    flag = 0
    try:
        while(True):
            ids = pickle.load(file)
            if(ids!=empid):
                pickle.dump(ids,tempFile)
            else:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                flag = 1
    except EOFError as e:
        if(flag==0):
            print("Employee Not Found!")
        else:
            print("Employee Deleted Successfully!")
        
    tempFile.close()
    file.close()
    os.remove("emp.dat")
    os.rename("temp.dat","emp.dat")
    input()

# FUNCTION TO COUNT ALL EMPLOYEE FROM A FILE.
def totalEmp():
    file = open("emp.dat","rb")
    add = 0
    try:
        while True:
            pickle.load(file)
            add=add+1
    except EOFError as e:
        print("\n\nTotal Employees :",add//4,"\n")
        input()
                

# DASHBOARD
while(True):
    print("\n\n **** EMPLOYEE MANAGEMENT SYSTEM ****\n")
    print("1. ADD AN EMPOYEE")
    print("2. VIEW ALL EMPLOYEE")
    print("3. VIEW AN EMPLOYEE BY ID")
    print("4. DELETE AN EMPLOYEE")
    print("5. NUMBER OF TOTAL EMPLOYEE")
    print("6. EXIT")
    ch = int(input("Enter Your Choice : "))
    if(ch==6):
        print("\nBye - Bye Admin!")
        break
    elif(ch==1):
        addEmp()
    elif(ch==2):
        viewAllEmp()
    elif(ch==3):
        viewById()
    elif(ch==4):
        delEmp()
    elif(ch==5):
        totalEmp()

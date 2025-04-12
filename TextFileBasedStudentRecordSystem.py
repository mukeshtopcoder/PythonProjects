# MINI PROJECT ON STUDENT DATABASE RECORD.
# CURD -> CREATE , UPDATE , READ , DELETE
def addStudent():
    file = open("stuDB.txt","a")
    name = input("Enter Student Name : ")
    mobile = input("Enter Mobile : ")
    add = input("Enter Location/Address : ")
    course = input("Enter Course :")
    st=name+"\n"+mobile+"\n"+add+"\n"+course+"\n"
    file.write(st)
    file.close()
    print("Student Data Recorded Successfully!\n")

def showStudent():
    file = open("stuDB.txt","r")
    data = file.readlines()
    i = 0
    for a in range(0,len(data)//4):
        print("Name :",data[i],end="")
        i=i+1
        print("Mobile :",data[i],end="")
        i=i+1
        print("Address :",data[i],end="")
        i=i+1
        print("Course : ",data[i],end="")
        i=i+1
        print("------------------------")


while(True):
    print("\n\n***** STUDENT DATABASE *****\n")
    print("1. Add Student")
    print("2. Show All Student")
    print("3. Exit")
    print("\nEnter Your Choice : ",end="")
    ch = int(input())
    if(ch==3):
        print("Bye-Bye User!")
        break
    elif(ch==1):
        addStudent()
    elif(ch==2):
        showStudent()
    
    

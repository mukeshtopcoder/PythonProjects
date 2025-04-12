#MySQL Connection
import mysql.connector
conn = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "553655",
database = "college"
    )
cur = conn.cursor()

# Method To Add A Student Into A Database
def addStudent():
    stuname = input("Enter Student Name : ")
    stuadd = input("Enter Student Address : ")
    stucourse = input("Enter Student Course Name : ")
    stumobile = input("Enter Student Mobile : ")
    try:
        sql = '''INSERT INTO student(stuname,stuadd,stucourse,
            stumobile) VALUE(%s,%s,%s,%s)'''
        value = (stuname,stuadd,stucourse,stumobile)
        cur.execute(sql,value)
        conn.commit()
        print(cur.rowcount,"Student Added Successfully!\n")
    except Exception as e:
        print("Error : ",e)

# Method To View All Students Data
def viewAllStudent():
    try:
        sql = "SELECT * FROM student";
        cur.execute(sql)
        result = cur.fetchall()
        print("Roll No\tName\tAddress\tCourse\tMobile")
        for a in result:
            print(a[0],"\t",a[1],"\t",a[2],"\t",a[3],"\t",a[4])
    except Exception as e:
        print("Error : ",e)

# Method To View A Student By Roll No
def viewStudentByRollNo():
    roll = input("\nEnter Student Roll No : ")
    try:
        sql = "SELECT * FROM student WHERE rollno = "+roll
        cur.execute(sql)
        result = cur.fetchall()
        if(len(result)!=0):
            for a in result:
                print("\nStudent Roll No : ",a[0])
                print("Student Name : ",a[1])
                print("Student Address : ",a[2])
                print("Student Course : ",a[3])
                print("Student Mobile : ",a[4])
        else:
            print("Student Not Found on This Roll No")
    except Exception as e:
        print("Error : ",e)

# Method To Delete A Student
def deleteStudent():
    roll = input("Enter Student Roll No To Delete : ")
    try:
        sql1="SELECT * FROM student WHERE rollno="+roll
        cur.execute(sql1)
        result=cur.fetchall()
        if(len(result)!=0):
            sql2="DELETE FROM student WHERE rollno="+roll
            cur.execute(sql2)
            conn.commit()
            print("Student Deleted Successfully!\n")
        else:
            print("\nStudent Not Found On This Roll No\n")
    except Exception as e:
        print("Error : ",e)

# Student Management Dashboard
start = 'Y'
while(start=='Y'):
    print("\n********* WELCOME **********\n")
    print("College Management System\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Student By Roll Number")
    print("4. Delete A Student")
    print("5. Exit")
    ch = input("\nEnter Your Choice : ")

    if(ch=='5'):
        start='N'
        print("Thank You For Using Our Software!")
    elif(ch=='1'):
        addStudent()
    elif(ch=='2'):
        viewAllStudent()
    elif(ch=='3'):
        viewStudentByRollNo()
    elif(ch=='4'):
        deleteStudent()
    else:
        print("Wrong Entered!\nPlease Try Again!")

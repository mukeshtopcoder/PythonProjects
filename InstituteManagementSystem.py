# Import mysql connector to connect with database
import mysql.connector
# Create an database Object
conn = mysql.connector.connect(
host="127.0.0.1",
user="root",
passwd="553655",
database="techvidya"
    )
# Create A Curson To Execute Query
cur = conn.cursor()

# START PROJECT FROM HERE

# Add Student Method
def addStudent():
    try:
        name = input("Enter Student Name : ")
        add = input("Enter Student Address : ")
        email = input("Enter Student Email : ")
        course = input("Enter Course Name : ")
        sql = '''INSERT INTO student(stuname,stuadd,email,course)
VALUE(%s,%s,%s,%s)'''
        data = (name,add,email,course)
        cur.execute(sql,data)
        conn.commit()
        print("Student Add Successfully!")
    except Exception as e:
        print("Error : ",e)

# View All Students Method
def viewAllStudents():
    try:
        query = "SELECT * FROM student"
        cur.execute(query)
        result = cur.fetchall()
        for stu in result:
            print("Roll No : STU",stu[0])
            print("Name :",stu[1])
            print("Address :",stu[2])
            print("Email :",stu[3])
            print("Course :",stu[4])
            print("********************")
    except Exception as e:
        print("Error : ",e)

# View Student By ID Method
def viewStudentById():
    try:
        id = input("\nEnter Student ID : ")
        sql = "SELECT * FROM student WHERE id="+id
        cur.execute(sql)
        result = cur.fetchall()
        if(len(result)!=0):
            for stu in result:
                print("Roll No :",stu[0])
                print("Name :",stu[1])
                print("Address :",stu[2])
                print("Email :",stu[3])
                print("Course :",stu[4])
                print("********************")
        else:
            print("\nStudent Not Found on This ID")
    except Exception as e:
        print("Error : ",e)

# Delete A Student Method
def deleteAstudent():
    try:
        id = input("\nEnter ID to Delete A Student : ")
        sql = "DELETE FROM student WHERE id="+id
        cur.execute(sql)
        conn.commit()
        if(int(cur.rowcount)==0):
            print("\nStudent Not Found!")
        else:
            print("\nStudent Deletion Success!")
    except Exception as e:
        print("Error : ",e)

# Create A DASHBOARD

ch = 'a'
while(True):
    print("\n******** WELCOME TO TECH VIDYA **********\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View A Student By ID")
    print("4. Delete A Student")
    print("5. Exit")
    ch = input("\nEnter Your Choice : ")
    if(ch=='5'):
        print("Bye-Bye")
        break
    elif(ch=='1'):
        addStudent()
    elif(ch=='2'):
        viewAllStudents()
    elif(ch=='3'):
        viewStudentById()
    elif(ch=='4'):
        deleteAstudent()
    else:
        print("\nWrong Entered! Try Again!\n")




# Inventory Management System

# Importing Libraries
import mysql.connector

# Creating A Connection and A Cursor To Perform SQL Queries
conn = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '553655',
database = 'stock'
    )
cur = conn.cursor()

# A Method to Add A Product
def addProduct():
    name = input("\n\tEnter Product Name : ")
    price = input("\tEnter Product Price : ")
    sql = "insert into product(pname,price) value('"+name+"',"+price+")"
    cur.execute(sql)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tProduct Added Successfully!")
    else:
        print("\n\tProduct Failed To Add!")
    input("\n\tPress Enter To Continue...")

# A Method to Add A Customer
def addCustomer():
    name = input("\n\tEnter Customer Name : ")
    add = input("\tEnter Customer Address : ")
    mob = input("\tEnter Customer Mobile Number : ")
    sql = "insert into customer(cname,cadd,cmob) value('"+name+"','"+add+"','"+mob+"')"
    cur.execute(sql)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tCustomer Added Successfully!")
    else:
        print("\n\tCustomer Failed To Add!")
    input("\n\tPress Enter To Continue...")

# A Method To Remove A Product
def removeProduct():
    sql = 'select * from product'
    cur.execute(sql)
    print("\n\tPID\tP_Name\t\tPrice\n")
    for pr in cur.fetchall():
        print("\t",pr[0],end="\t")
        print(pr[1],end="\t\t")
        print(pr[2])
    pid = input("\n\tEnter Product ID To Delete :")
    sql = 'delete from product where pid='+pid
    cur.execute(sql)
    conn.commit()
    if cur.rowcount > 0:
        print("\nProduct Removed Successfully!")
    else:
        print("\nProduct Removing Failed!")
    input("\n\tPress Enter Key To Continue..")

# Dashboard
while True:
    print("\n\n\t***** INVENTORY MANAGEMENT SYSTEM *****")
    print("\n\t1. Add Product")
    print("\t2. Add Customer")
    print("\t3. Remove Product")
    print("\t4. Place An Order")
    print("\t5. View Orders By Customer")
    print("\t6. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if ch == 6:
        print("\n\tThank For Using Our Management System!")
        break
    elif ch==1:
        addProduct()
    elif ch==2:
        addCustomer()
    elif ch==3:
        removeProduct()

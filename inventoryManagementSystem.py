# Inventory Management System

# Importing Libraries
import mysql.connector

# Creating A Connection and A Cursor To Perform SQL Queries
conn = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '553655',
database = 'store'
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
        print("\n\tProduct Removed Successfully!")
    else:
        print("\n\tProduct Removing Failed!")
    input("\n\tPress Enter Key To Continue..")

# A Method to check A Customer Exist or Not
def CheckCustomer(cid):
    sql = "SELECT * FROM customer WHERE cid="+cid
    cur.execute(sql)
    data = cur.fetchall()
    return data

def CheckProduct(pid):
    sql = "SELECT * FROM product WHERE pid="+pid
    cur.execute(sql)
    data = cur.fetchall()
    return data

# A Method to place An Order
def placeAnOrder():
    cid = input("\n\tEnter Customer ID : ")
    cus = CheckCustomer(cid)
    if len(cus) != 0:
        print("\n\tCustomer Name : ",cus[0][1])
        print("\tCustomer Address : ",cus[0][2])
        print("\tCustomer Mobile : ",cus[0][3])
        pid = input("\n\tEnter Product ID : ")
        pro = CheckProduct(pid)
        if len(pro) != 0:
            print("\n\tProduct Name : ",pro[0][1])
            print("\tProduct Price : ",pro[0][2])
            qty = input("\n\tEnter Quantity You Want To Buy : ")
            sql = 'insert into orders(cid,pid,qty) value(%s,%s,%s)'
            data = (cid,pid,qty)
            cur.execute(sql,data)
            conn.commit()
            if cur.rowcount>0:
                print("\n\tOrder Placed Successfully!")
            else:
                print("\n\tFailed To Place An Order!")
        else:
            print("\n\tProduct Does Not Exist!")
    else:
        print("\n\tCustomer Does Not Exist!")
    input("\n\tPress Enter To Continue...")

# A Method to view an order by Customer ID
def viewOrder():
    cid = input("\n\tEnter Customer ID : ")
    if len(CheckCustomer(cid)) != 0:
        sql = '''SELECT cname,cadd,pname,price,qty,qty*price FROM customer c
                    JOIN orders o 
                    ON c.cid = o.cid
                    JOIN product p
                    ON o.pid = p.pid WHERE c.cid='''+cid
        cur.execute(sql)
        data = cur.fetchall()
        if len(data) != 0:
            print("\n\tCustomer Name : ",data[0][0])
            print("\tCustomer Address : ",data[0][1])
            print("\tProduct Name : ",data[0][2])
            print("\tProduct Price : ",data[0][3])
            print("\tProduct Quantity : ",data[0][4])
            print("\t-----------------------------")
            print("\tAmount : ",data[0][5])
            print("\t-----------------------------")
        else:
            print("\n\tNo Orders Found on This Customer ID!")
    else:
        print("\n\tThere is no order on this ID!")
    input("\n\tPress Enter To Continue...")

# Dashboard
while True:
    print("\n\n\t***** INVENTORY MANAGEMENT SYSTEM *****")
    print("\n\t1. Add Product")
    print("\t2. Add Customer")
    print("\t3. Remove Product")
    print("\t4. Place An Order")
    print("\t5. View Orders By Customer ID")
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
    elif ch==4:
        placeAnOrder()
    elif ch==5:
        viewOrder()
    else:
        input("\n\tWrong Entered!\n\tTry Again!\n\tPress Enter To Continue...")

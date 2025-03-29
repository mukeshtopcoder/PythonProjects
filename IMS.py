# Inventory Management System

# REQUIRED LIBRARIES
import mysql.connector

# A MySQL Connection And Cursor
conn = mysql.connector.connect(
host = '127.0.0.1',
user = 'root',
password = '553655',
database = 'store'
    )
cur = conn.cursor()

# A Method To Add A Product
def addProduct():
    pname = input("\n\tEnter Product Name : ")
    price = input("\tEnter Product Price : ")
    sql = "insert into product(pname,price) value(%s,%s)"
    data = (pname,price)
    cur.execute(sql,data)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tProduct Added Successfully!")
    else:
        print("\n\tProduct Addition Failed!")
    input("\n\tPress Enter To Continue...")

# A Method To Add A Customer
def addCustomer():
    cname = input("\n\tEnter Customer Name : ")
    cadd = input("\tEnter Customer Address : ")
    sql = "insert into customer(cname,cadd) value(%s,%s)"
    data = (cname,cadd)
    cur.execute(sql,data)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tCustomer Added Successfully!")
    else:
        print("\n\tCustomer Addition Failed!")
    input("\n\tPress Enter To Continue...")

# Check Existance of a Customer By ID
def checkCustomer(cid):
    sql = 'select * from customer where cid='+cid
    cur.execute(sql)
    return cur.fetchall()

# Check Existance of a Product By ID
def checkProduct(pid):
    sql = 'select * from product where pid='+pid
    cur.execute(sql)
    return cur.fetchall()


# A Method To Place An Order
def placeAnOrder():
    cid = input("\n\tEnter Customer ID : ")
    data = checkCustomer(cid)
    if len(data) != 0:
        print("\n\tCustomer Name : ",data[0][1])
        print("\tCustomer Address : ",data[0][2])
        pid = input("\n\tEnter Product ID : ")
        pdata = checkProduct(pid)
        if len(pdata) != 0:
            print("\n\tProduct Name : ",pdata[0][1])
            print("\tProduct Price : ",pdata[0][2])
            qty = input("\n\tEnter Product Quantity You Want To Buy : ")
            sql = 'insert into orders(cid,pid,qty) value(%s,%s,%s)'
            data = (cid,pid,qty)
            cur.execute(sql,data)
            conn.commit()
            if cur.rowcount > 0:
                print("\n\tOrder Placed Succssfully!")
            else:
                print("\n\tFailed To Order Place!")
        else:
            print("\n\tProduct is Not Available on This ID!")
    else:
        print("\n\tCustomer is Not Available on This ID!")
    input("\n\tPress Enter To Continue...")

# A Method to View All Orders
def viewAllOrders():
    sql = """select cname,cadd,pname,price,qty from customer c
                    join orders o
                    on c.cid = o.cid
                    join product p 
                    on o.pid = p.pid;"""
    cur.execute(sql)
    data = cur.fetchall()
    for order in data:
        print("\n\t"+order[0]+"\t"+order[1]+"\t"+order[2]+"\t"+str(order[3])+"\t"+str(order[4]))
    input("\n\tPress Enter To Continue...")

# A Method to View An Order
def viewOrder():
    cid = input("\n\tEnter Customer ID  : ")
    data = checkCustomer(cid)
    if len(data) != 0:
        sql = """
            select cname,cadd,pname,price,qty,price*qty from customer c
            join orders o
            on c.cid = o.cid
            join product p
            on o.pid = p.pid WHERE c.cid ="""+cid
        cur.execute(sql)
        order = cur.fetchall()
        for data in order:
            print("\n\tCustomer Name : ",data[0])
            print("\tCustomer Add : ",data[1])   
            print("\tProduct Name : ",data[2])   
            print("\tProduct Price : ",data[3])   
            print("\tProduct Quantity : ",data[4])
            print("\t-----------------------------------------")
            print("\tTotal Amount : ",data[5])
            print("\t------------------------------------------")
    else:
        print("\n\tCustomer ID is invalid!")
    input("\n\tPress Enter To Continue...")

# A Method to delete a product
def deleteProduct():
    pid = input("\n\tEnter Product ID : ")
    sql = "delete from product where pid="+pid
    cur.execute(sql)
    conn.commit()
    if cur.rowcount > 0 :
        print("\n\tProduct Removed Successfully!")
    else:
        print("\n\tProduct is Not Available on This ID!")
    input("\n\tPress Enter To Continue...")

# Dashboard
while True:
    print("\n\t***** INVENTORY MANAGEMENT SYSTEM *****")
    print("\n\t1. Add Product")
    print("\t2. Add Customer")
    print("\t3. Delete Product")
    print("\t4. Place An Order")
    print("\t5. View All Orders")
    print("\t6. View An Order By Customer ID")
    print("\t7. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if ch==7:
        print("\n\tThank You For Using Our Software!")
        break
    elif ch==1:
        addProduct()
    elif ch==2:
        addCustomer()
    elif ch==3:
        deleteProduct()
    elif ch==4:
        placeAnOrder()
    elif ch==5:
        viewAllOrders()
    elif ch==6:
        viewOrder()
    else:
        input("\n\tWrong Entered!\n\tTry Again By Pressing Enter Button!")










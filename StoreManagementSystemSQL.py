# Store Management System

# IMPORTING LIBRARIES
import mysql.connector
# Class for database connection
class DBConnect:
    # method for creating an mysql object
    @staticmethod
    def getConnection():
        conn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "553655",
            database = "store"
            )
        return conn

# Class for customer related methods
class Customer:
    # Method to View All Customer Details
    @staticmethod
    def viewCustomers():
        sql = "SELECT * FROM customer"
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        print("\n\tAll Customer Details Are Here!\n")
        for cus in data:
            print("\t",cus[0],cus[1],cus[2],cus[3])
        input("\n\n\t--- Press Enter To Continue...")
        
    # Method to get a customer by ID
    @staticmethod
    def getCustomer(cid):
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM customer WHERE cid = "+cid
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        conn.close()
        if(data!=None):
            return data
        else:
            return None
    
    # Method to add a customer
    @staticmethod
    def addCustomer():
        name = input("\n\tEnter Customer Name : ")
        add = input("\tEnter Customer Address : ")
        mobile = input("\tEnter Customer Mobile Number : ")
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        sql = "INSERT INTO customer(cname,cadd,cmobile) VALUE(%s,%s,%s)"
        data = (name,add,mobile)
        cur.execute(sql,data)
        if(cur.rowcount==1):
            print("\n\tCustomer Added Successfully!")
        else:
            print("\n\tWe are unable to add Customer Right Now!")
        input("\n\t--- Press Enter To Continue!...")
        conn.commit()
        cur.close()
        conn.close()
        
# Class for product related methods
class Product:
    # Method to get product by ID
    def getProduct(pid):
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM product WHERE pid = "+pid
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        conn.close()
        if(data!=None):
            return data
        else:
            return None
    
    # Method to add a product
    @staticmethod
    def addProduct():
        name = input("\n\tEnter Product Name : ")
        price = input("\tEnter Product Price : ")
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        sql = "INSERT INTO product(pname,price) VALUE(%s,%s)"
        data = (name,price)
        cur.execute(sql,data)
        conn.commit()
        if(cur.rowcount==1):
            print("\n\tProduct Addedd Sucessfully!")
        else:
            print("\n\tUnable to add Product At this time!...")
        input("\n\t--- Press Enter To Continue...")
        cur.close()
        conn.close()

# Class for orders related method
class Orders:
    # Method To View An Order
    @staticmethod
    def viewOrder():
        cid = input("\n\tEnter Customer ID : ")
        sql = '''
        select c.cid,c.cname,cadd,cmobile,p.pid,p.pname,price,
        o.qty,o.qty*price from customer c
        join orders o
        on c.cid = o.cid
        join product p
        on o.pid = p.pid WHERE c.cid = 
        '''+cid
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        if(data!=None):
            print("\n\tCustomer Details")
            print("\tCustomer ID : ",data[0])
            print("\tCustomer Name : ",data[1])
            print("\tCustomer Address : ",data[2])
            print("\tCustomer Mobile Number : ",data[3])
            print("\n\tProduct Details")
            print("\tProduct ID : ",data[4])
            print("\tProduct Name : ",data[5])
            print("\tProduct Price : ",data[6])
            print("\tProduct Quantity : ",data[7])
            print("\tNet Amount : ",data[8])
        else:
            print("\n\tNo Orders Found on this Customer ID")
        cur.close()
        conn.close()
        input("\n\t--- Press Enter To Continue...")
    
    # Method for place an order
    @staticmethod
    def placeOrder():
        cid = input("\n\tEnter Customer ID : ") 
        cus = Customer.getCustomer(cid)
        if(cus!=None):
            print("\n\tCustomer Name : ",cus[1])
            print("\tCustomer Address : ",cus[2])
            pid = input("\n\tEnter Product ID : ")
            pro = Product.getProduct(pid)
            if(pro!=None):
                print("\n\tProduct Name : ",pro[1])
                print("\tProduct Price : ",pro[2])
                qty = input("\n\tEnter Quantity : ")
                conn = DBConnect.getConnection()
                cur = conn.cursor()
                sql = "INSERT INTO orders(cid,pid,qty) VALUE(%s,%s,%s)"
                data = (cid,pid,qty)
                cur.execute(sql,data)
                conn.commit()
                if(cur.rowcount>0):
                    print("\n\tOrder Placed Successfully!")
                else:
                    print("\n\tUnable to place your order currently!")
                cur.close()
                conn.close()
            else: 
                print("\n\tProduct Not Available on This Product ID")
        else:
            print("\n\tCustomer Not Available on This Customer ID")
        input("\n\tPress Enter To Continue...")
        
    
class Main:
    # Method for Dashboard
    @staticmethod
    def __init__():
        while True:
            print("\n\t***** STORE MANAGEMENT SYSTEM*****")
            print("\n\t1. Add Customer")
            print("\t2. Add Product")
            print("\t3. Place An Order")
            print("\t4. View An Order")
            print("\t5. View All Customers")
            print("\t6. Exit")
            ch = int( input("\n\tEnter Your Choice  : ") )
            if(ch==6):
                print("\n\tBye-Bye Admin!")
                break
            elif(ch==1):
                Customer.addCustomer()
            elif(ch==2):
                Product.addProduct()
            elif(ch==3):
                Orders.placeOrder()
            elif(ch==4):
                Orders.viewOrder()
            elif(ch==5):
                Customer.viewCustomers()
            else:
                input("\n\tWrong Enter! Try Again!")

Main()

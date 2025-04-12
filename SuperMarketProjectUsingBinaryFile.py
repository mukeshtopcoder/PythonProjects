# SUPER MARKET PROJECT IN PYTHON USING BINARY FILE.

import pickle
import os
# FUNCTION TO ADD A PRODUCT
def addProduct():
    file = open("store.dat","ab")
    pid = input("\n\tEnter Product ID : ")
    pname = input("\tEnter Product Name : ")
    price = input("\tEnter Product Price : ")
    qty = input("\tEnter Number of Products (Qty) : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    pickle.dump(qty,file)
    print("\n\tProduct Added Successfully!")
    input("\n\t-- Press Enter To Continue...")
    file.close()

# FUNCTION TO PRINT ALL THE PRODUCTS
def viewAllProduct():
    file = open("store.dat","rb")
    count = 0
    print("\nPID P_Name Price Qty")
    try:
        while True:
            print(pickle.load(file),end=" ")
            print(pickle.load(file),end=" ")
            print(pickle.load(file),end=" ")
            print(pickle.load(file))
    except:
        print("\n\tAll The Products Are Here!")
        input("\n\t-- Press Enter To Continue...")
    file.close()

# FUNCTION TO VIEW A PRODUCT BY ID
def viewProduct():
    file = open("store.dat","rb")
    pid = input("\n\tEnter Product ID : ")
    proFound = 0
    try:
        while True:
            data = pickle.load(file)
            if(data==pid):
                print("\n\tProduct ID : ",data)
                print("\tProduct Name : ",pickle.load(file))
                print("\tProduct Price : ",pickle.load(file))
                print("\tProduct Qty : ",pickle.load(file))
                proFound = 1
    except:
        if(proFound==0):
            print("\n\tProduct Not Found!")
        else:
            print("\n\tHere is Your Product!")
        input("\n\t-- Press Enter To Continue!")
    file.close()

# FUNCTION TO DELETE A PRODUCT
def delProduct():
    file1 = open("store.dat","rb")
    temp = open("temp.dat","ab")
    pid = input("\n\tEnter Product ID To Delete : ")
    proFound = 0
    try:
        while True:
            data = pickle.load(file1)
            if(data==pid):
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                proFound = 1
            else:
                pickle.dump(data,temp)
    except:
        if(proFound==0):
            print("\n\tProduct Not Found!")
        else:
            print("\n\tProduct Deleted Successfully!")
        input("\n\t-- Press Enter To Continue...")
    temp.close()
    file1.close()
    os.remove("store.dat")
    os.rename("temp.dat","store.dat")

# FUNCTION TO UPDATE A PRODUCT
def updateProduct():
    file = open("store.dat","rb")
    temp = open("temp.dat","ab")
    proFound = 0
    pid = input("\n\tEnter Product ID : ")
    try:
        while True:
            data = pickle.load(file)
            if(data==pid):
                pickle.dump(data,temp)
                name = pickle.load(file)
                print("\n\tID : ",data)
                print("\tProduct Name : ",name)
                pickle.dump(name,temp)
                price = input("\tEnter Price : ")
                qty = input("\tEnter Quantity : ")
                pickle.dump(price,temp)
                pickle.dump(qty,temp)
                pickle.load(file)
                pickle.load(file)
                proFound = 1
            else:
                pickle.dump(data,temp)
    except:
        if(proFound==0):
            print("\n\tProduct Not Found!")
        else:
            print("\n\tProduct Updated Successfully!")
        input("\n\t-- Press Enter To Continue...")
    file.close()
    temp.close()
    os.remove("store.dat")
    os.rename("temp.dat","store.dat")

# DASHBOARD
while True:
    print("\n\t*** SUPER MARKET SOFTWARE ***")
    print("\n\t1. Add Product")
    print("\t2. View All Product")
    print("\t3. View A Product By Product ID")
    print("\t4. Delete A Product")
    print("\t5. Update A Product")
    print("\t6. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if(ch==6):
        print("\n\t--- Bye-Bye Admin!")
        break
    elif(ch==1):
        addProduct()
    elif(ch==2):
        viewAllProduct()
    elif(ch==3):
        viewProduct()
    elif(ch==4):
        delProduct()
    elif(ch==5):
        updateProduct()
    else:
        print("\n\tWorng Entered!")
        input("\n\tPress Enter To Try Again!...")

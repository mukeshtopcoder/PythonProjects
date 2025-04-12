#Hospital Management System

#Required Libraries
import mysql.connector

#Making a connection with MySQL
class DBconnect:
    @staticmethod
    def getConnection():
        conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "553655",
    database = "hospital"
        )
        return conn


#Patient entity
class Patient:
    def __init__(self,pid,pname,padd,pdis):
        self.pid = pid
        self.pname = pname
        self.padd = padd
        self.pdisease = pdis

    #Add A Patient
    @staticmethod 
    def addPatient():
        name = input("\n\tEnter Patient Name : ")
        add = input("\n\tEnter Patient Address : ")
        dis = input("\n\tEnter Patient Disease : ")
        sql = "insert into patient(pname,padd,pdis) value(%s,%s,%s)"
        data = (name,add,dis)
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        print("\n\tPatient Added Successfully!")
        input("\n\t---Press Enter To Continue...")
        conn.close()
        cur.close()

    # A Method to view all patient
    @staticmethod
    def viewAllPatient():
        sql = "select * from patient"
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        print("\n\tPID\tP_Name\tP_Add\tP_Disease")
        for doc in data:
            print("\t"+str(doc[0])+"\t"+doc[1]+"\t"+doc[2]+"\t"+doc[3])
        conn.close()
        cur.close()
        input("\n\t--- Press Enter To Continue...")
    @staticmethod
    def getPatient(pid):
        sql = "select * from patient where pid="+pid
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        conn.close()
        cur.close()
        if(data!=None):
            return data
        else:
            return None


#Doctor Entity and Dao
class Doctor:
    def init(self,did,danme,dspec):
        self.did = did
        self.dname = dname
        self.dspec = dspec

    @staticmethod
    def addDoctor():
        name = input("\n\tEnter Doctor Name : ")
        spec = input("\n\tEnter Doctor Specification : ")
        sql = "insert into doctor(dname,spec) value(%s,%s)"
        data = (name,spec)
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        print("\n\tDoctor Added Successfully!")
        input("\n\t---Press Enter To Continue...")
        conn.close()
        cur.close()

    @staticmethod
    def getDoctor(did):
        sql = "select * from doctor where did="+did
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        conn.close()
        cur.close()
        if(data!=None):
            return data
        else:
            return None

# Appointment Class
class Appoint:
    @staticmethod
    def bookAnAppoint():
        pid = input("\n\tEnter Patient ID to Book Appointment : ")
        pat = Patient.getPatient(pid)
        if(pat!=None):
            did = input("\n\tEnter Doctor ID to Book Appointment : ")
            doc = Doctor.getDoctor(did)
            if(doc!=None):
                print("\n\tPatient Name : ",pat[1])
                print("\tPatient Address : ",pat[2])
                print("\tPatient Disease : ",pat[3])
                print("\n\t****************************")
                print("\tDoctor Name : ",doc[1])
                print("\tDoctor Specification : ",doc[2])
                date = input("\n\tEnter Appointment Date (yyyy/mm/dd): ")
                sql = "insert into appoint(pid,did,adate) value(%s,%s,%s)"
                data = (pid,did,date)
                conn = DBconnect.getConnection()
                cur = conn.cursor()
                cur.execute(sql,data)
                conn.commit()
                cur.close()
                conn.close()
                print("\n\tAppointment Booked Successfully!")
            else:
                print("\n\tDoctor Not Available On This ID")
        else:
            print("\n\tPatient not available on this ID")
        input("\n\t--- Press Enter To Continue!..")
    @staticmethod
    def viewAppoint():
        pid = input("\n\tEnter Patient ID : ")
        sql = '''
        SELECT patient.pname,patient.padd,patient.pdis,doctor.dname,
        doctor.spec,appoint.adate FROM patient
        JOIN appoint
        ON patient.pid = appoint.pid
        JOIN doctor
        ON doctor.did = appoint.did
        WHERE patient.pid ='''+pid
        conn = DBconnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        if(data!=None):
            print("\n\tPatient Name : ",data[0])
            print("\tPatient Address : ",data[1])
            print("\tPatient Disease : ",data[2])
            print("\tDoctor Name : ",data[3])
            print("\tDoctor Specification : ",data[4])
            print("\tAppointment Date : ",data[5]) 
        else:
            print("\n\tNo Appointment Found on this patient ID")
        conn.close()
        cur.close()
        input("\n\t--- Press Enter To Continue...")
        

#Main class with Dashboard
class Main:
    @staticmethod
    def __init__():
        while True:
            print("\n\t**Hospital Management System**")
            print("\n\t1.Add Patient")
            print("\t2.View All Patient")
            print("\t3.Book An Appointment")
            print("\t4.View A Patient or Appointment")
            print("\t5.Add Doctor")
            print("\t6.Exit")
            ch = int(input("\n\tEnter your choice:"))
            if(ch==6):
                print("\n\t---Bye-Bye Admin!")
                break
            elif(ch==1):
                Patient.addPatient()
            elif(ch==2):
                Patient.viewAllPatient()
            elif(ch==3):
                Appoint.bookAnAppoint()
            elif(ch==4):
                Appoint.viewAppoint()
            elif(ch==5):
                Doctor.addDoctor()

Main()

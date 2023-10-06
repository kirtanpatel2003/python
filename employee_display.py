# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:59:41 2020

@author: Kirtan
"""

import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists employee")
mycursor.execute("use employee")
mycursor.execute("create table if not exists empl_details(emp_no char(4) primary key,name varchar(30),dept char(20),mobileno char(10))")
mydb.commit()
while True:
    print("1--> Create record")
    print("2--> Display all records")
    print("0--> Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        try: 
            EMP_NO=str(input("Enter employee number:"))
            NAME=input("Enter name(limit 35 characters):")
            DEPT=str(input("Enter department name:"))
            MN=str(input("Enter mobile no.:"))
            mycursor.execute("insert into empl_details values('"+EMP_NO+"','"+NAME+"','"+DEPT+"','"+MN+"')")
            mydb.commit()
            print("Account is successfully created!!!")
        except: 
            print("""
                  Error in creating record...
                  """)
    elif ch==2:
        try: 
            mycursor.execute("select * from empl_details")
            rec=mycursor.fetchall()
            print(tabulate(rec,headers=["emp_no","name","dept","mobileno"],tablefmt="fancy_grid"))
        except:
            print("Error in Displaying record")
    elif ch==0:
        break
    else:
        print("""
              Enter Valid Choice...
              """)

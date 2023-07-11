# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:27:21 2020

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
while(True):
    
    print("1--> Search record")
    print("0--> Exit")
    ch=int(input("Enter your choice:"))
    
    if ch == 1:
        try:
            emp_no=str(input("Enter employee number to be displayed : "))
            mycursor.execute("select * from empl_details where emp_no = '"+emp_no+"'")
            rec=mycursor.fetchall()
            print(tabulate(rec,headers=["emp_no","name","city","mobileno","balance"],tablefmt="fancy_grid"))
        except:
            print("""
                  Error in Displaying record...
                  """)
            
    elif ch==0:
        break
    
    else:
        print("""
              Enter Valid Choice...
              """)
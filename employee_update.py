# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:37:26 2020

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
    
    print("1--> Update record")
    print("0--> Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        try:
            emp_no=str(input("Enter Employee Number of Record To Be Updated : "))
            name=input("Enter name(limit 35 characters):")
            dept=str(input("Enter department name:"))
            mn=str(input("Enter mobile no.:"))
            print(tabulate(headers=["emp_no","name","city","mobileno","balance"],tablefmt="fancy_grid"))

        except:
            print("Record Not Updated" )
            
    elif ch==0:
        break
    
    else:
        print(" Enter a  Valid Choice ")
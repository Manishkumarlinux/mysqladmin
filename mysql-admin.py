#!/usr/bin/python

import os
import sys
import MySQLdb

print "1 = create database"
print "2 = restore db nackup"
print "3 = take db backup"

DBADMIN = 'root'
ADMINPASS = 'redhat'

Q = int(input("Please Enter Your Choice: "))

if Q == 1:
    nm = raw_input("Enter DB Name: ")
    ur = raw_input("Enter User Name: ")
    pa = raw_input("Enter Password: ")
    host = 'localhost'
    db1 = MySQLdb.connect(host="localhost",user="root",passwd="redhat")
    cursor = db1.cursor()
    sql ="""CREATE DATABASE %s""" % nm
    gn =('grant all privileges on %s.* to %s@localhost identified by "%s"' % (nm, ur, 'pa'))
    uc ="CREATE USER '%s'@'%s' " %(ur, host)
    pas ="SET PASSWORD FOR '%s'@'%s' = '%s'" %(ur, host, pa)
    auth ="GRANT ALL ON %s.* TO '%s'@'%s'" %(nm, ur, host)
    cursor.execute(sql)
    cursor.execute(uc)
    cursor.execute(pas)
    cursor.execute(auth)
if Q == 2:
    nm = raw_input("Enter DB Name: ")
    bf = raw_input("Backup File Name: ")
    restorecmd = "mysql -u " + DBADMIN + " -p" + ADMINPASS + " " + nm + " < " + bf
    os.system(restorecmd)

if Q == 3:
    nm = raw_input("Enter DB Name: ")
    bkf = raw_input("Enter Backup File Name: ")
    bkpcmd = "mysqldump -u " + DBADMIN + " -p" + ADMINPASS + " " + nm + " > " + bkf
    os.system(bkpcmd)

else:
    print "ckeck error"

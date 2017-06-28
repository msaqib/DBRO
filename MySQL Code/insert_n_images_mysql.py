#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import psycopg2
import sys
import MySQLdb

def read_image(i):
    
    filename="/home/faban/Downloads/Python/Python-Mysql/images/im"
    filename=filename+str(i)+".jpg"
    print(filename)
    fin = open(filename)    
    img = fin.read()
    
    return img



con = MySQLdb.connect("192.168.50.12","root","faban","experiments" )  
with con:
    print('connecting to database')
    range_from=input('Enter range from:')
    range_till=input('Enter range till:')
    for i in range(range_from,range_till):
     cur = con.cursor()
     data = read_image(i)
     cur.execute("INSERT INTO images VALUES(%s, %s)", (i,data, ))
     cur.close()
     con.commit()
con.close()

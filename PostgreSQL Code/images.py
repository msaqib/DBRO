#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con=None

def readImage(i):

    try:
        filename="/home/faban/Downloads/Python/Python-Mysql/images/im"
        filename=filename+str(i)+".jpg"
        print (filename)
        fin = open(filename, "rb")
        img = fin.read()
        return img
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

try:
    con = psycopg2.connect("host=192.168.50.12 dbname=postgres user=postgres password=faban sslmode=disable")     
    cur = con.cursor()
    #cur.execute("Drop table if exists images")
   # j=input("Enter images from:")
   # k=input("Enter images Till:")
    for i in range (1,500):
     data = readImage(i)
     binary = psycopg2.Binary(data)
     cur.execute("INSERT INTO Images(Id, Data) VALUES (%s, %s)", (i,binary,) )
     con.commit()    
    # con.close()
except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e    
    sys.exit(1)
    
finally:    
    if con:
        con.close() 

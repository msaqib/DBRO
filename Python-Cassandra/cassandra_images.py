#!/usr/bin/python
# -*- coding: utf-8 -*-
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import SimpleStatement
import sys

#reading my hostname, username, and password from the command line; defining my Cassandra keyspace as as variable.
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
keyspace="excelsior"

#adding my hostname to an array, setting up auth, and connecting to Cassandra
nodes = []
nodes.append(hostname)
auth_provider = PlainTextAuthProvider(username=username, password=password)
ssl_opts = {}
cluster = Cluster(nodes,auth_provider=auth_provider,ssl_options=ssl_opts)
session = cluster.connect(keyspace)

#setting my image name, loading the file, and reading the data
def read_image(i):
    
    filename="/home/faban/Downloads/Python/Python-Mysql/images/im"
    filename=filename+str(i)+".jpg"
    print(filename)
    fin = open(filename)    
    img = fin.read()
    
    return img



  
with session:
    print('connecting to database')
    session.execute("Drop table if exists images")
    session.execute("create table images(id int primary key, data blob)")
    print('Table Created Successfully') 
    range_from=input('Enter range from:')
    range_till=input('Enter range till:')
    for i in range(range_from,range_till):
     
     data = read_image(i)
     strCQL = "INSERT INTO images (id,data) VALUES (?,?)"
     pStatement = session.prepare(strCQL)
     session.execute(pStatement,[i,data])
session.shutdown()

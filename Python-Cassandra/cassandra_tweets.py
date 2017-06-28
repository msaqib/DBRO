#!/usr/bin/python
# -*- coding: utf-8 -*-
#import psycopg2
import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import SimpleStatement
import sys
#reading my hostname, username, and password from the command line; defining my Cassandra keyspace as as variable.
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
keyspace="mydb"

#adding my hostname to an array, setting up auth, and connecting to Cassandra
nodes = []
nodes.append(hostname)
auth_provider = PlainTextAuthProvider(username=username, password=password)
ssl_opts = {}
cluster = Cluster(nodes,auth_provider=auth_provider,ssl_options=ssl_opts)
session = cluster.connect(keyspace)



filename="/home/faban/Downloads/Python/Python-Mysql/tweets.csv"
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)





 session.execute("Drop table if exists Tweets")

 session.execute("create table Tweets(a text primary key,b text, c text,d text,e text, f text,g text,h text, i text, j text)")
 print('Table Created Successfully')
 count=0
 for row in csv_data:
 #print(row)
  a=row[0]
  b=row[1]
  c=row[2]
  d=row[3]
  e=row[4]
  f=row[5]
  g=row[6]
  h=row[7]
  i=row[8]
  j=row[9]
  print('Inserted Row Number: ',count)
  count=1+count
  strCQL = "INSERT INTO Tweets (a,b,c,d,e,f,g,h,i,j) VALUES (?,?,?,?,?,?,?,?,?,?)"
  pStatement = session.prepare(strCQL)
  session.execute(pStatement,[a,b,c,d,e,f,g,h,i,j])
  print('Data populated successfully')
session.shutdown()

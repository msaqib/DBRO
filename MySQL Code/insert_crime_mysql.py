#import psycopg2
import csv
import MySQLdb

# Open database connection

filename="/home/faban/Downloads/Python/Python-Mysql/Crime.csv"
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)

#csv_data = csv.reader(file('/home/faban/Python-Postgresql/Crime.csv'))

 db = MySQLdb.connect("192.168.50.12","root","faban","experiments" )
 cursor = db.cursor()
 cursor.execute("Drop table if exists Crime")
#print("Table created successfully")
 cursor.execute("create table Crime(a text,b text, c text,d text,e text, f text,g text,h text, i text)")
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
  print('Inserted Row Number: ',count)
  count=1+count
  cursor.execute('insert into Crime values ("%s","%s","%s","%s","%s","%s","%s","%s","%s")' %(a,b,c,d,e,f,g,h,i))
  db.commit()
db.close()

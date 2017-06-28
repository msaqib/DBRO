import psycopg2
import csv
import MySQLdb
filename='/home/faban/Downloads/Python/Python-Mysql/tweets.csv'
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)

#csv_data = csv.reader(file('/home/faban/Python-Postgresql/Crime.csv'))

 database = MySQLdb.connect("192.168.50.12","root","faban","experiments" )
 cursor = database.cursor()
#cursor.execute("Create Table tweet (name text, city text, country text)")
#print("Table created successfully")
 cursor.execute("Drop table if exists Tweets")
 cursor.execute("create table Tweets(a text,b text, c text, d text, e text, f text, g text, h text, i text, j text)")
 print('Table Created Successfully')
 count=0
 for row in csv_data:
  
#  if count>=3:
   #   break   
  #print(row)
  user=row[0]
  b=row[1]
  c=row[2]
  timestamp=row[3]
  source=row[4]
  tweet=row[5]
  g=row[6]
  h=row[7]
  i=row[8]
  j=row[9] 
  #print(row)
  count=1+count
  print('Inserting Row Number: ',count)
  cursor.execute("INSERT INTO Tweets VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user,b,c,timestamp,source,tweet,g,h,i,j))
# csv_data.close()
 # cursor.close()
  database.commit()
database.close()

print "CSV data imported"

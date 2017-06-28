import psycopg2
import csv
filename='/home/faban/Downloads/Python/Python-Postgre/Crime.csv'
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)

#csv_data = csv.reader(file('/home/faban/Python-Postgresql/Crime.csv'))

 database = psycopg2.connect("host=192.168.50.12 dbname=postgres user=postgres password=faban sslmode=disable")     
 cursor = database.cursor()
#cursor.execute("Create Table tweet (name text, city text, country text)")
#print("Table created successfully")
 cursor.execute("Drop table if exists Crime")
 cursor.execute("create table Crime(a text,b text, c text, d text, e text, f text, g text, h text, i text)")
 print('Table Created Successfully')
 count=0
 for row in csv_data:
  
#  if count>=3:
   #   break   
  #print(row)
  name=row[0]
  city=row[1]
  country=row[2]
  d=row[3]
  e=row[4]
  f=row[5]
  g=row[6]
  h=row[7]
  i=row[8]
  print('Row Insered :',count)
  count=1+count
 # print(count)
  cursor.execute("INSERT INTO Crime VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,city,country,d,e,f,g,h,i))
# csv_data.close()
 cursor.close()
 database.commit()
database.close()

print "CSV data imported"

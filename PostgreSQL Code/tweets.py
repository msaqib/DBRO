import psycopg2
import csv
filename='/home/faban/Downloads/Python/Python-Postgre/tweets.csv'
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)

#csv_data = csv.reader(file('/home/faban/Python-Postgresql/Crime.csv'))

 database = psycopg2.connect("host=192.168.50.12 dbname=postgres user=postgres password=faban sslmode=disable")     
 cursor = database.cursor()
 count_row=0
 cursor.execute("Drop table if exists Tweets")
 cursor.execute("create table Tweets(a text,b text, c text, d text, e text, f text, g text, h text, i text, j text)")
 print('Table Created Successfully') 
 for row in csv_data:  
  name=row[0]
  city=row[1]
  country=row[2]
  d=row[3]
  e=row[4]
  tweet=row[5]
  g=row[6]
  h=row[7]
  i=row[8]
  j=row[9] 
  print("Inserted row number:",count_row)
  count_row=1+count_row
 # print(count)
  cursor.execute("INSERT INTO Tweets VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,city,country,d,e,tweet,g,h,i,j))
# csv_data.close()
# cursor.close()
  database.commit()
database.close()

print "CSV data imported"

import psycopg2
import csv
import math
#from math import 
filename='/home/faban/Downloads/TestJava/tweets.csv'
with open (filename,'rU') as csvfile:
 csv_data=csv.reader(csvfile)
 csv_data2=csv.reader(csvfile)

#csv_data = csv.reader(file('/home/faban/Python-Postgresql/Crime.csv'))

# database = psycopg2.connect (host= "192.168.40.12",database = "postgres", user="postgres", password="faban")
# cursor = database.cursor()
#cursor.execute("Create Table tweet (name text, city text, country text)")
#print("Table created successfully")
# cursor.execute("create table Tweets(a text,b text, c text, d text, e text, tweet text, g text, h text, i text, j text)")
# print('Table Created Successfully')
 count_row=0
 max_tweet_length=0
 avg_tweet_length=0
 max_row=0
 min_tweet_length=300
 min_row=0
 mean_sum=0
 total_characters=0
 mean_dif=0
 for row in csv_data:
  
#  if count>=3:
   #   break   
  print(row)
  name=row[0]
  city=row[1]
  country=row[2]
  d=row[3]
  e=row[4]
  tweet=row[5]
  tweet_length=len(tweet)
  mean_diff=tweet_length-87
  print('mean diff is ',mean_diff)
  mean_sum=mean_sum+pow(mean_diff,2)
  print ("mean_sum is :",mean_sum)
  total_characters=tweet_length+total_characters
  g=row[6]
  h=row[7]
  i=row[8]
  j=row[9] 
 # print(tweet_length)
  count_row=1+count_row
  if tweet_length>max_tweet_length:
   max_tweet_length=tweet_length
   max_row=count_row 
  if tweet_length<min_tweet_length:
   min_tweet_length=tweet_length
   min_row=count_row 
 avg_tweet_length=total_characters/count_row
 
 # print(count)
#  cursor.execute("INSERT INTO Tweets VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,city,country,d,e,tweet,g,h,i,j))
# csv_data.close()
# cursor.close()
# database.commit()
#database.close()
print('Number of rows :',count_row)
#print('Maximum tweet length :', max_tweet_length,'at row no :',max_row)
#print("Total characters :",total_characters)
#print('Number of rows :',count_row)
#print('Minimum tweet length :', min_tweet_length,'at row no :',min_row)
#avg_tweet_length=total_characters/count_row
#print('Average tweet length is:',avg_tweet_length)
#standard_dev=mean_sum/count_row
#standard_dev=standard_dev**(1.0/2)
#print('standard deviation is :',standard_dev)
#print('Mean sum is :',mean_sum)

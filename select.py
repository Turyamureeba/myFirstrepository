#Import the python driver for PostgreSQL
import psycopg2


try:
   connection = psycopg2.connect(user="postgres",
                                  password="killer999",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from pai"
   conn = None
   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from Pai table using cursor.fetchall")
   pai_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in pai_records:
   	 

       print("ID=",row[0],)
       print("Food=",row[1],)
       print("Number=",row[2],"\n")
       row.shape

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
        if conn is not None:
            conn.close()


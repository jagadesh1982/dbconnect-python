import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='books',
                                         user='root',
                                         password='Redhat123@')

   
    input = raw_input("Do you Want to add Authors the Existing Authors (Y/N) : ")    
    
    while (input != 'Y' and input != 'N' and input != 'y' and input != 'n'):
       input = raw_input("error: wrong input. Please put Y/y or N/n only ")
    
    if input.lower() == 'y':
        if connection.is_connected():
           name = raw_input("Enter the Author Name : ")
           book_name = raw_input("Enter the Book Name : ")
           email = raw_input("Enter Email : ")
           cursor = connection.cursor()
           sql = "INSERT INTO authors (id,name,book_name,email) VALUES(1,%s,%s,%s)"
           val = (name,book_name,email)
           cursor.execute(sql,val)  
           cursor.close()
           connection.commit()
    elif input.lower() == 'n':
        if (connection.is_connected()):
          connection.close()
        exit
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
        print("MySQL connection is closed Successfully")

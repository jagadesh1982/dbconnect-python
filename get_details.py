import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='books',
                                         user='root',
                                         password='Redhat123@')
    
    input = raw_input("Do you Want to View the Existing Authors (Y/N) : ")    
    
    while (input != 'Y' and input != 'N' and input != 'y' and input != 'n'):
       input = raw_input("error: wrong input. Please put Y/y or N/n only ")
    
    if input.lower() == 'y':
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL Server version ", db_Info)
           cursor = connection.cursor()
           cursor.execute("SELECT * FROM authors") 
           results = cursor.fetchall()
           for x in results:
              print(x)
           cursor.close()
    elif input.lower() == 'n':
        if (connection.is_connected()):
          connection.close()
        exit
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
        print("MySQL connection is closed Successfully")

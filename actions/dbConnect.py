# This is a simple module to fetch data from MySQL db.
# python -m pip install mysql-connector //run this command if you face import error
# references: https://www.w3schools.com/python/python_mysql_getstarted.asp

import traceback
import json
import mysql.connector

def getData(query:str):
        """
         @query: sql query that needs to be executed.

         returns the data being executed in "List" format
        """
        try:
            # Setup the connection.
            # Pass your database details here
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="chatbot"
                )
            # set up the cursor to execute the query
            cursor = mydb.cursor()
            cursor.execute(query)

            # fetch all rows from the last executed statement using `fetchall method`.
            results = cursor.fetchall()
            print(results)
            #output=""
            #print(len(results))
            #for i in range(0, len(results)):
            #    output+= results[i][0] + "\n"
            #print(output)
            return results
        except:
            print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))
            return []

#getData("SELECT Service_Name FROM services")
#getData("SELECT Description FROM services WHERE Service_Name LIKE 'Blood%'")
#getData("SELECT Description FROM 'services' WHERE Service_Name='Blood Test'")
# test the file before integrating with the bot by uncommenting the below line.
#print(getData("SELECT * FROM Testdb.Names;");
def getDataTwoParam(query:str, query2:str):
        """
         @query: sql query that needs to be executed.

         returns the data being executed in "List" format
        """
        try:

            # Setup the connection.
            # Pass your database details here
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="chatbot"
                )
            # set up the cursor to execute the query
            cursor = mydb.cursor()
            cursor.execute(query, query2)

            # fetch all rows from the last executed statement using `fetchall method`.
            results = cursor.fetchall()
            print(results)
            #output=""
            #print(len(results))
            #for i in range(0, len(results)):
            #    output+= results[i][0] + "\n"
            #print(output)
            return results
        except:
            print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))
            return []

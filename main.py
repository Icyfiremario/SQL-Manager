import sqlite3
from sqlite3 import Error
import sys
import os

userSel = 0
querySel = 0
customQuery = ""
newName = ""
delDatabase = ""

curConnection = None
database = None
create_users_table = "CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTERGER, gender TEXT, nationality TEXT);"
create_users = "INSERT INTO users(name, age, gender, nationality) VALUES ('James', 15, 'male', 'USA'), ('Katelyn', 13, 'female', 'USA')"

tables = None
databases = os.listdir("databases")

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection success")
    except Error as e:
        print(f"Error: {e}")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: {e}")

def generate_database(name):
    try:
        sqlite3.connect(f"databases/{name}.db")
        print(f"{name}.db created")
    except Error as e:
        print(f"Error: {e}")

while userSel != 7:
    print("----Selection an Option----")
    print("1. Connect to Database\n2. Execute query\n3. Show stored tables\n4. Create new database\n5. delete database\n6. list databases\n7. Exit\n")

    userSel = int(input())
    print("\n")

    if userSel == 1:
        database = input("Path to database:\n")
        curConnection = create_connection(database)
        tables = execute_read_query(curConnection, "SELECT name FROM sqlite_master WHERE type='table';")
    
    elif userSel == 2:
        if(curConnection == None):
            print("No Database loaded")
        else:
            print("----Preset Queries----")
            print("1.Create users table\n2. Create users\n3. Custom query\n")
            querySel = int(input())

            if querySel == 1:
                execute_query(curConnection, create_users_table)
            elif querySel == 2:
                execute_query(curConnection, create_users)
            elif querySel == 3:
                print("Input query below: \n")
                customQuery = input()
                execute_query(curConnection, customQuery)
    elif userSel == 3:
        if curConnection == None:
            print("Not connected to database")
        else:
            print(tables)
    elif userSel == 4:
        print("New database name:\n")
        newName = input()
        generate_database(newName)
    elif userSel == 5:
        print("Select a database to delete\n")
        print(f"{databases} \n")
        delDatabase = input()
        if os.path.exists(f"databases/{delDatabase}"):
            os.remove(f"databases/{delDatabase}")
        else:
            print("Database doesn't exist")
    
    elif userSel == 6:
        print(f"{databases} \n")

    elif userSel == 7:
        break
    else:
        print("Not an option.")


print("Exiting")
sys.exit()
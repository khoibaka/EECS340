from utils.sql2python import SQL2PYTHON
import sqlite3 as sql

conn = sql.connect('./database/cook_book.db')
cursor = conn.cursor()

sql_parser = SQL2PYTHON('./database/cook_book.db')


sql_parser.close()
while(True):
    print("""Enter a command from the following options: 
            create recipe
            create ingredient
            quit
            """)
    command = input().lower()
    
    if command == "create recipe":
        name = input("Enter the Name of the recipe: ")
        total_calories = input("Enter the total calories in the recipe: ")
        total_calories = int(total_calories)
        instructions = input("Enter the instructions for the recipe: ")

        cursor.execute("""INSERT INTO recipes(name, total_calories, instruction) 
                        VALUES(?,?,?)""",(name,total_calories,instructions))
    if command == "quit":
        break

conn.commit()
conn.close()
        
        


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
            create diet
            create utensil
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

        print("Recipe added.")

    elif command == "create ingredient":
        name = input("Enter the Name of the ingredient: ")
        shelf_life = input("Enter the shelf life of ingredient in days: ")
        shelf_life = int(shelf_life)
        calories_density = input("Enter the calorie density for the recipe: ")
        calories_density = int(calories_density)
        cursor.execute("""INSERT INTO ingredients(name, shelf_life, calorie_density) 
                        VALUES(?,?,?)""",(name,shelf_life,calories_density))
        print("Ingredient added")

    elif command == "create utensil":
        name = input("Enter the Name of the utensil: ")
        cursor.execute("""INSERT INTO utensils(name) 
                        VALUES(?)""",(name))
        print("Utensil added")

    elif command == "create diet":
        name = input("Enter the Name of the diet: ")
        cursor.execute("""INSERT INTO diets(name) 
                        VALUES(?)""",(name))
        print("Diet added")
    elif command == "quit":
        break
    else:
        print("Command not in system")
conn.commit()
conn.close()
        
        


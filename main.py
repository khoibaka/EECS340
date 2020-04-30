from utils.sql2python import SQL2PYTHON
import sqlite3 as sql
from add_command import add_command
from utils.helper import find_id_from_name, show_recipe_from_id
conn = sql.connect('./database/cook_book.db')
cursor = conn.cursor()


while(True):
    print("""Enter a command from the following options: 
            (1) create recipe
            (2) create ingredient
            (3) create diet
            (4) create utensil
            (5) edit recipe
            (6) show recipe
            (7) quit
            """)
    command = input().lower()
    
    if command == "create recipe" or command == '1':
        name = input("Enter the Name of the recipe: ")
        total_calories = input("Enter the total calories in the recipe: ")
        total_calories = int(total_calories)
        instructions = input("Enter the instructions for the recipe: ")

        cursor.execute("""INSERT INTO recipes(name, total_calories, instruction) 
                        VALUES(?,?,?)""",(name,total_calories,instructions))

        print("Recipe added.")
        conn.commit()

    elif command == "create ingredient" or command == '2':
        name = input("Enter the Name of the ingredient: ")
        shelf_life = input("Enter the shelf life of ingredient in days: ")
        shelf_life = int(shelf_life)
        calories_density = input("Enter the calorie density for the ingredient: ")
        calories_density = int(calories_density)
        cursor.execute("""INSERT INTO ingredients(name, shelf_life, calorie_density) 
                        VALUES(?,?,?)""",(name,shelf_life,calories_density))    #SQL
        print("Ingredient added")
        conn.commit()

    elif command == "create utensil" or command == '4':
        name = input("Enter the Name of the utensil: ")
        cursor.execute("""INSERT INTO utensils(name)        
                        VALUES(?)""",(name,))               #SQL
        print("Utensil added")
        conn.commit()

    elif command == "create diet" or command == '3':
        name = input("Enter the Name of the diet: ")
        cursor.execute("""INSERT INTO diets(name)           
                        VALUES(?)""",(name,))               #SQL
        print("Diet added")
        conn.commit()

    elif command == "add into recipes" or command == '5':
        cursor.execute("SELECT * FROM recipes")             #SQL
        print("choose a recipe to add to:")
        rows = cursor.fetchall()
        for row in rows:
            print("             " +row[1])
        recipe_name = input()
        recipe_id = find_id_from_name(rows,recipe_name)
        while(recipe_id == -1):
            recipe_name = input("Cannot find recipe, check spelling and type again or type cancel to exit:")
            if(recipe_name == 'cancel'):
                break
            recipe_id = find_id_from_name(rows,recipe_name)
        
        sub_command = input("""Choose a command from these command
                            (1) add ingredients
                            (2) add diets
                            (3) add utensils
        """)
        add_command(cursor, sub_command, recipe_id)
        conn.commit()

    elif command == 'show recipe' or command == '6':
        cursor.execute("SELECT * FROM recipes")             #SQL
        print("choose a recipe to show:")
        rows = cursor.fetchall()
        for row in rows:
            print("             " +row[1])
        recipe_name = input()
        recipe_id = find_id_from_name(rows,recipe_name)
        while(recipe_id == -1):
            recipe_name = input("Cannot find recipe, check spelling and type again or type cancel to exit:")
            if(recipe_name == 'cancel'):
                break
            recipe_id = find_id_from_name(rows,recipe_name)
        show_recipe_from_id(cursor,recipe_name)


    elif command == "quit" or command == '7':
        break

    else:
        print("Command not in system")
conn.commit()
conn.close()
        
        


from utils.sql2python import SQL2PYTHON
import sqlite3 as sql
from add_command import add_command
from utils.helper import find_id_from_name
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
            (7) search
            (8) quit
            """)
    command = input().lower()
    
    if command == "create recipe" or command == '1':
        name = input("Enter the Name of the recipe: ").lower()
        total_calories = input("Enter the total calories in the recipe: ")
        total_calories = int(total_calories)
        instructions = input("Enter the instructions for the recipe: ").lower()

        cursor.execute("""INSERT INTO recipes(name, total_calories, instruction) 
                        VALUES(?,?,?)""",(name,total_calories,instructions))

        print("Recipe added.")
        conn.commit()

    elif command == "create ingredient" or command == '2':
        name = input("Enter the Name of the ingredient: ").lower()
        shelf_life = input("Enter the shelf life of ingredient in days: ")
        shelf_life = int(shelf_life)
        calories_density = input("Enter the calorie density for the ingredient: ")
        calories_density = int(calories_density)
        cursor.execute("""INSERT INTO ingredients(name, shelf_life, calorie_density) 
                        VALUES(?,?,?)""",(name,shelf_life,calories_density))    #SQL
        print("Ingredient added")
        conn.commit()

    elif command == "create utensil" or command == '4':
        name = input("Enter the Name of the utensil: ").lower()
        cursor.execute("""INSERT INTO utensils(name)        
                        VALUES(?)""",(name,))               #SQL
        print("Utensil added")
        conn.commit()

    elif command == "create diet" or command == '3':
        name = input("Enter the Name of the diet: ").lower()
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
        recipe_name = input().lower()
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
        recipe_name = input().lower()
        recipe_id = find_id_from_name(rows,recipe_name)
        while(recipe_id == -1):
            recipe_name = input("Cannot find recipe, check spelling and type again or type cancel to exit:")
            if(recipe_name == 'cancel'):
                break
            recipe_id = find_id_from_name(rows,recipe_name)
        print(rows[recipe_id - 1])



    elif command == "search" or command == '7':
        print("""Enter a type of search from the following options: 
            (1) recipe name
            (2) diet name
            (3) single ingredient
            (4) two ingredients
            (5) one ingredient excluding another
            """)
        command = input().lower()
        
        if command == 'recipe name' or command =='1':
            
            name = input("Enter the name of the recipe you are searching for: ").lower()

            cursor.execute("SELECT * FROM recipes WHERE name = ?", (name,))
            rows = cursor.fetchall()
            for row in rows:
                print("             " +row[1])
        
        elif command == 'diet name' or command == '2':

            name = input("Enter the name of the diet you are searching for: ").lower()

            cursor.execute("SELECT r.name FROM recipes r, diets d, suitable s WHERE d.name = ? AND s.dietName = d.name AND r.id = s.recipesID", (name,))
            rows = cursor.fetchall()
            for row in rows:
                print("             " +row[0])

        elif command == 'single ingredient' or command == '3':
            name = input("Enter the name of the ingredient you are searching for: ").lower()
    
            cursor.execute("""SELECT r.name 
                                FROM recipes r, contains c, ingredients i 
                                WHERE i.name = ? AND i.name = c.ingredientName AND r.id = c.recipesID""", (name,))
            rows = cursor.fetchall()
            for row in rows:
                print("             " +row[0])
            
        elif command== 'two ingredients' or command == '4':
            name1 = input("Enter the name of the first ingredient you are searching for: ").lower()
            name2 = input("Enter the name of the second ingredient you are searching for: ").lower()
    
            cursor.execute("""SELECT r.name 
                                FROM recipes r, contains c1, contains c2, ingredients i1, ingredients i2 
                                WHERE i1.name = ? AND i2.name = ? AND r.id = c1.recipesID AND r.id = c2.recipesID AND 
                                c1.ingredientName = i1.name AND c2.ingredientName = i2.name""", (name1,name2))
            rows = cursor.fetchall()
            for row in rows:
                print("             " +row[0])

        elif command== 'one ingredient excluding another' or command == '5':
            name1 = input("Enter the name of the ingredient you are searching for: ").lower()
            name2 = input("Enter the name of the ingredient you are excluding: ").lower()
    
            cursor.execute("""SELECT r.name 
                                FROM recipes r, contains c, ingredients i
                                WHERE r.id = c.recipesID AND i.name = ? AND i.name = c.ingredientName
                                EXCEPT SELECT r2.name
                                        FROM recipes r2, contains c2, ingredients i2
                                        WHERE r2.id = c2.recipesID AND c2.ingredientName = i2.name AND i2.name = ?
                                
                                
                                """, (name1,name2))
            rows = cursor.fetchall()
            for row in rows:
                print("             " +row[0])
            show = input("Enter the name of the recipe you want to show: ")

    elif command == "quit" or command == '8':
        break

    else:
        print("Command not in system")
conn.commit()
conn.close()
        
        


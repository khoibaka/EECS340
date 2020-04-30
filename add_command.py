from utils.helper import find_id_from_name,check_name_pk

def add_command(cursor, command,recipe_id):
    if(command == 'add ingredients' or command == '1'):
        cursor.execute("SELECT * from ingredients")
        rows = cursor.fetchall()
        print("Choose an ingredient in these ingredients:")
        for row in rows:
            print("                 " + row[0])
        ingredient_name = input()
        while(not check_name_pk(rows, ingredient_name)):
            if(ingredient_name == "cancel"):
                break
            ingredient_name = input("Cannot find ingredient, check spelling and type again or type 'cancel' to exit:")
        cursor.execute("""INSERT INTO contains(ingredientName, recipesID)
                        VALUES(?,?)""",(ingredient_name, recipe_id))
        print("Ingredient added")

    elif(command == 'add diets' or command == '2'):
        cursor.execute("SELECT * from diets")
        rows = cursor.fetchall()
        print("Choose a diet in these diets:")
        for row in rows:
            print("                 " + row[0])
        diet_name = input()
        while(not check_name_pk(rows, diet_name)):
            if(diet_name == "cancel"):
                break
            diet_name = input("Cannot find diet, check spelling and type again or type 'cancel' to exit:")
        cursor.execute("""INSERT INTO suitable(dietName, recipesID)
                VALUES(?,?)""",(diet_name, recipe_id))
        print("Diet added")

    elif(command == 'add utensils' or command == '3'):
        cursor.execute("SELECT * from utensils")
        rows = cursor.fetchall()
        print("Choose a utensil in these utensils: ")
        for row in rows:
            print("                 " + row[0])
        utensil_name = input()
        while(not check_name_pk(rows, utensil_name)):
            if(utensil_name == "cancel"):
                break
            utensil_name = input("Cannot find utensil, check spelling and type again or type 'cancel' to exit:")
        time = input("Utensil using time in minute: ")
        time = int(time)
        action = input("Action with utensil: ")
        temperature = input("Temprerature for that action: ")
        temperature = int(temperature)

        cursor.execute("""INSERT INTO utensils_usage(utensilName, recipesID, time, action, temparature)
                VALUES(?,?,?,?,?)""",(utensil_name, recipe_id, time, action, temperature))
        print("Diet added")
    else:
        pass 




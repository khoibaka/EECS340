
def find_id_from_name(rows, name):
    for row in rows:
        if(row[1] == name):
            return row[0]
    return -1

def check_name_pk(rows,name):
    for row in rows:
        if(row[0] == name):
            return True
    return False

def show_recipe_from_id(cursor, name):
    cursor.execute("SELECT * FROM recipes WHERE name=?", (name,))
    recipe = cursor.fetchall()[0]
    
    print("""
    
    /------------------------------------------------/""")
    print(recipe[1])
    print(f'Cook time: {recipe[2]} minute')
    print(f'Instruction: {recipe[3]}')
    print("Ingredients: ")
    cursor.execute("""SELECT c.ingredientName
                    FROM contains c
                    WHERE c.recipesID=?""", (recipe[0],))
    rows = cursor.fetchall()
    for row in rows:
        print(f' - {row[0]}')

    print("Suiable diets:")
    cursor.execute("""SELECT s.dietName
                    FROM suitable s
                    WHERE s.recipesID=?""", (recipe[0],))
    rows = cursor.fetchall()
    for row in rows:
        print(f' - {row[0]}')

    print("Utensil used: ")
    cursor.execute("""SELECT u.utensilName
                    FROM utensils_usage u
                    WHERE u.recipesID=?""", (recipe[0],))
    rows = cursor.fetchall()
    for row in rows:
        cursor.execute("""SELECT u.utensilName
                    FROM utensils_usage u
                    WHERE u.recipesID=?""", (recipe[0],))
        print(f' - {row[0]}')
    print("""
    
    /------------------------------------------------/""")
    
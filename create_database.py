import sqlite3 as sql
from utils.sql2python import SQL2PYTHON

def main():
    sql_parser = SQL2PYTHON('./database/cook_book.db')
    
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS ingredients (name TEXT PRIMARY KEY, shelf_life INTEGER, calorie_density INTEGER)')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, total_calories INTEGER, instruction '
        'TEXT)')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS diets (name TEXT PRIMARY KEY)')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS utensils (name TEXT PRIMARY KEY)')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS contains (ingredientName TEXT, recipesID INTEGER, FOREIGN KEY (ingredientName) '
        'REFERENCES ingredients(name), FOREIGN KEY (recipesID) REFERENCES recipes(id))')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS suitable (dietName TEXT, recipesID INTEGER, FOREIGN KEY (dietName) '
        'REFERENCES diets(name), FOREIGN KEY (recipesID) REFERENCES recipes(id))')
    sql_parser.run(
        'CREATE TABLE IF NOT EXISTS utensils_usage (utensilName TEXT, recipesID INTEGER, time INTEGER, action TEXT, '
        'temperature INTEGER, FOREIGN KEY (utensilName) REFERENCES utensils(name), FOREIGN KEY (recipesID) REFERENCES '
        'recipes(id))')
    sql_parser.close()

if __name__ == '__main__':
    main()
import sqlite3 as sql
from utils.sql2python import SQL2PYTHON

def main():
    sqlParser = SQL2PYTHON('./database/cook_book.db')
    sqlParser.run('CREATE TABLE IF NOT EXISTS ingredients (name TEXT PRIMARY KEY, shelf_life INTEGER, calorie_density '
                  'INTEGER)')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS ingredients (name TEXT PRIMARY KEY, shelf_life INTEGER, calorie_density INTEGER)')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name TEXT, total_calories INTEGER, instruction '
        'TEXT)')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS diets (name TEXT PRIMARY KEY)')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS utensils (name TEXT PRIMARY KEY)')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS contains (ingredientName TEXT, recipesID INTEGER, FOREIGN KEY (ingredientName) '
        'REFERENCES ingredients(name), FOREIGN KEY (recipesID) REFERENCES recipes(id))')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS suitable (dietName TEXT, recipesID INTEGER, FOREIGN KEY (dietName) '
        'REFERENCES diets(name), FOREIGN KEY (recipesID) REFERENCES recipes(id))')
    sqlParser.run(
        'CREATE TABLE IF NOT EXISTS utensils_usage (utensilName TEXT, recipesID INTEGER, time INTEGER, action TEXT, temparature INTEGER, FOREIGN KEY (utensilName) '
        'REFERENCES utensils(name), FOREIGN KEY (recipesID) REFERENCES recipes(id))')
    sqlParser.close()

if __name__ == '__main__':
    main()
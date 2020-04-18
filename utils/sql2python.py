import sqlite3 as sql

class SQL2PYTHON:
    def __init__(self, db_name):
        self.__db_name = db_name
        self.__open_database(db_name)

    #Helper to open back the database after closed
    def __open_database(self,db_name):
        self.__conn = sql.connect(db_name)
        self.__c = self.__conn.cursor()
        self.__closed = False

    #Run the command from args
    def run(self, command):
        if(self.__closed):
            self.__open_database(self.__db_name)
        self.__c.execute(command)

    #Close the database after used
    def close(self):
        self.__conn.commit()
        self.__c.close()
        self.__conn.close()
        self.__closed = True

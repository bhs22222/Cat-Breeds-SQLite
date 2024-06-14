import sqlite3

DATABASE = 'Cat Breeds.db'


def print_Cat_Breeds_Lifespan():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Breed, Lifespan FROM Cat Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} Lifespan : {Cat_Breeds[1]}")


def print_Coat_pattern_Weight():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Coat_pattern, Weight FROM Cat Breeds;"
        cursor.execute(sql)
        results = cursor.ftchall()
        for Cat_Breeds in results:
            print(f"Coat_pattern:{Cat_Breeds[0]} Weight : {Cat_Breeds[1]}")


def print_Type_Height():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Type, Height FROM Cat Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()

        for Cat_Breeds in results:
            print(f"Type:{Cat_Breeds[0]} Height : {Cat_Breeds[1]}")



import sqlite3

DATABASE = 'Cat Breeds.db'

        
def print_Cat_Breeds_location_of_origin():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed,location_of_origin FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely
        
        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} location of origin : {Cat_Breeds[1]}")
               
               
def print_Cat_Breeds_type():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, type FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} type : {Cat_Breeds[1]}")
            
            
def print_Cat_Breeds_body_type():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, body_type FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} body type : {Cat_Breeds[1]}")
            
            
def print_Cat_Breeds_coat_type_and_length():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, coat_type_and_length FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} coat type and length : {Cat_Breeds[1]}")
            
            
def print_Cat_Breeds_coat_pattern():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, coat_pattern FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} coat pattern : {Cat_Breeds[1]}")
            
                  
def print_Cat_Breeds_lifespan():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, lifespan FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} lifespan : {Cat_Breeds[1]}")
            
             
def print_Cat_Breeds_length():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed,length FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} length : {Cat_Breeds[1]}")
            
            
def print_Cat_Breeds_height():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, height FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely

        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} height : {Cat_Breeds[1]}")


def print_Cat_Breeds_weight():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT breed, Weight FROM Cat_Breeds;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print them nicely
    
        for Cat_Breeds in results:
            print(f"Cat Breeds:{Cat_Breeds[0]} Weight : {Cat_Breeds[1]}")

input_1 = input("Would you like to know the information about Cat Breeds?")

input_1 = input_1.lower()

#if input_1 not in ["yes", "no"]:
while input_1 not in ["yes", "no"]:
    print("This is an invaild answer, please enter either yes or no.")
    input_1 = input("Would you like to know the information about Cat Breeds?")
    input_1 = input_1.lower()
    
else:
    if input_1 == 'no':
        print("Thanks for your visit!")
        
    elif input_1 == 'yes':

        print("What information would you like to know?")
        print("1. location")
        print("2. type")
        print("3. body type")
        print("4. coat type and length")
        print("5. coat pattern")
        print("6. lifespan")
        print("7. length")
        print("8. height")
        print("9. weight")
        
        #input_2 = int(input("which information do you want to know, please give me a number between 1 to 9"))
        input_2 = input("which information do you want to know, please give me a number between 1 to 9. ")
        
        #if input_2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        while input_2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("This is an invaild answer, please enter a number between 1 and 9.")
            input_2 = input("which information do you want to know, please give me a number between 1 to 9. ")
            
        if int(input_2) ==1:
        # print out all the information about breed 1
        #print_breed_1_height
        #print_breed_1_weight
            print_Cat_Breeds_location_of_origin()
            
        elif int(input_2) ==2:
            print_Cat_Breeds_type()
            
        elif int(input_2) ==3:
            print_Cat_Breeds_body_type()
            
        elif int(input_2) ==4:
            print_Cat_Breeds_type()
            
        elif int(input_2) ==5:
            print_Cat_Breeds_coat_pattern()

        elif int(input_2) ==6:
            print_Cat_Breeds_lifespan()
            
        elif int(input_2) ==7:
            print_Cat_Breeds_length()
            
        elif int(input_2) ==8:
            print_Cat_Breeds_height()
            
        else:
            print_Cat_Breeds_weight()
        # print out all the information about breed 1
import random
drinks = ["vodka", "gin", "rum", "tequila", "beer", "wine", "seltzer", "whiskey"]
try:
    name= input("What is your name? ")
    age= input("How old are you? ")
    country= input("Where are you from? ")
    age= int(age) # convert string to integer
except ValueError:
    print("Invalid age. Please enter a number")
else:
    if age < 0 or age > 140:
        print("You are not human. This game is for human only.")
    elif age > 120:
        print("You are too old to play the awsome drinking game.")
    elif age < 18:
        print("You are a minor. You can not play the awsome drinking game.")
    elif (country == "USA" or country == "UAE") and age < 21:
        print("You are not allowed to drink in USA or UAE. You can not play the awsome drinking game.")
    else:
        print("You are an adult. You can play awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game")

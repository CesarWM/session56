import random
lives = 3
while lives:
    print("You have", lives, "lives left.")
    # roll the dice
    dice = random.randint(1,6)
    print("You rolled a", dice)
    # check if you win
    if dice == 6:
        print("\nYou win!\n")
        break
    lives -= 1
else:
    print("\nYOU LOOSE!\n")
print("Thank you for playing. Goodbye.")

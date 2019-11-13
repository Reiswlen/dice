import random

sides = input("How many sides to the die? (enter 0 to quit)\n")

while sides != 0:   
    if sides == 'd20':
        print ("You have rolled a **20**")
    else:
        sides = int(sides)
        print ("You have rolled a **" + (str(random.randint(1, sides))+ "**"))
    sides = input("How many sides to the die? (enter 0 to quit)\n")
   
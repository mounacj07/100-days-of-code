print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("Choose your direction: Left or Right? ").lower()
if direction=="left":
    cross=input("There is an island at the middle of a lake. Type 'swim' to swim across or 'wait' to wait for a boat. ").lower()
    if cross=="wait":
        door=input("You have reached the island. There are three doors in front of you. Which one do you choose? Red, Blue or Yellow? ").lower()
        if door=="red":
            print("You have been burned by fire.\nGame over.")
        elif door=="blue":
            print("You have been eaten by beasts.\nGame over.")
        elif door=="yellow":
            print("Congratulations!. You found the treasure. You win!")
        else:
            print("Oops! That's not a door.\nGame over.")
    else:
        print("You were attacked by a trout.\nGame over.")
else:
    print("You fall into a hole.\nGame over.")
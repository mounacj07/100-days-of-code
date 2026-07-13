import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions=[rock, paper, scissors]
print("Are you ready for a game of rock, paper, scissors?")
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
random_num = random.randint(0, 2)
if(user_input>=0 and user_input<3):
    print(f"You:\n{actions[user_input]}")
    computer_input = actions[random_num]
    print(f"Computer:\n{computer_input}")
else:
    print("Invalid input. You lose.")

if(user_input==random_num):
    print("The match is a draw.")
elif((user_input==0 and random_num==1) or (user_input==1 and random_num==2) or (user_input==2 and random_num==0)):
    print("You lose.")
elif((user_input==1 and random_num==0) or (user_input==2 and random_num==1) or (user_input==0 and random_num==2)):
    print("You win.")

import random

user_win=0
system_win=0
options=["rock","paper","scissor"]

while True:
    user_input=input("Enter rock.paper/scissor/q: ").lower()
    if user_input=='q':
        break
    elif user_input not in options:
        print("Please enter valid input")
        continue

    computer_input=random.randint(0,2)
    #0 : rock 1 : paper 2 : scissor

    computer_pick=options[computer_input]
    print("Computer picked",computer_pick)

    if user_input=='rock' and computer_pick=='scissor':
        print("You won!")
        user_win+=1
    elif user_input=='paper' and computer_pick=='rock':
        print("You won!")
        user_win+=1
    elif user_input=='scissor' and computer_pick=='paper':
        print("You won")
        user_win+=1
    else:
        print("You lost!")
        system_win+=1

print("You win",user_win,"times.")
print("Computer wins",system_win,"times.")

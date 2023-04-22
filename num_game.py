import random
no_chances=7
start=1
stop=50
n=random.randint(start,stop)

for _ in range(0,no_chances+1):
    i = int(input("Guess a num: "))
    if _>=no_chances and i!=n:
        print("Better Luck Next Time!")
    elif i>stop or i>n:
        print("Try Again! Your guess is too high")
    elif i<n or i<start:
        print("Try Again! Your guess is too small")
    elif i==n:
        print("Congrats! Your guess is correct")
        break


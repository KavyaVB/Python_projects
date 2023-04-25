print("WWelcome to Quiz game")

response=input("Do you wwant to play? ")

if response.lower()!='yes':
    quit()
else:
    print("Okay Let's play")
score=0
count=0
answer=input("What is the full form of API? ")
if answer.title()=='Application Programming Interface':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
count+=1

answer=input("What is the full form of ROM? ")
if answer.title()=='Read Only Memory':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
count+=1

answer=input("What is the full form of DVM? ")
if answer.title()=='Dalvik Virtual Machine':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
count+=1

answer=input("What is the full form of JVM? ")
if answer.title()=='Java Virtual Machine':
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
count+=1

print("Your score is: "+str((score/count)*100)+"%")

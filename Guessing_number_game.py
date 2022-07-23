import random
number=random.randint(1,100)
attempts=0
while(True):
    guess=int(input("Enter the number: "))
    if guess<number:
        print("enter higher number")
        attempts+=1
    elif guess>number:
        print("enter lower number")
        attempts+=1
    else:
        print(f"congrates you guessed the number in {attempts+1} attempt")
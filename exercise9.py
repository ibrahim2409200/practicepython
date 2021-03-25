#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
a=random.randint(1,9)
i=True
count=0
while i==True:
    n = int(input("Guess the number:\n"))
    print(a)
    if n==a:
        print("Hurray you got it right")
        count += 1
    else:
        print("Ohh you lost!")
    e=str(input("Do you want to play agin? press exit or yes.\n"))
    if e=="exit":
        i=False
    else:
        i=True
print("You got",count,"right answers")
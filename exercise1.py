#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
enterloop=1

while (enterloop==1):
    name=str(input("Enter name:"))
    age=int(input("Enter age:"))
    n=100-age
    year=2021+n
    print(name.upper()," your 100th birthday will be in the year",year)
    ques=int(input("You want to check one more time?\nPress 1 for again check or press 0 to stop:\n"))
    if (ques==1):
        enterloop= 1
    else:
        enterloop= 0
        print("Thankyou!")

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
n=int(input("Enter a nummber:"))
if n%4==0:
    print("The number is multiple of 4 and is an even number.")
elif (n%2==0):
    print(n,"is an even number.")
else:
    print(n,"is an odd number.")
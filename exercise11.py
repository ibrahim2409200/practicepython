#Ask the user for a number and determine whether the number is prime or not.
def get_number():
    return int(input("Enter number:\n"))
a=get_number()
for i in range(2,a):
    if (a%i==0):
        print("Not prime")
        break
else:
    print("Prime")

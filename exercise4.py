#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number
n=int(input("Enter Range Number:"))
dl=[]
for i in range(1,n+1):
    if (n%i==0):
        dl.append(i)
print(dl)

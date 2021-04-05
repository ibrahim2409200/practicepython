#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
def fib_nums(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<=0:
        print("Invalid input")
    else:
        print(a)
        print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)
x=int(input("Enter numbers of fibonacci numbers you want?"))
fib_nums(x)
#Ask the user for a string and print out whether this string is a palindrome or not.
a=str(input("Enter the string:"))
r=a[::-1]#for reversing the string we use [::-1]
if a==r:
    print("Palindrome")
else:
    print("Not pallindrome")
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
n=int(input("Enter number:"))
a=[1,1,2,3,5,8,13,21,34,55,89]
nl= []
for i in a:
    if i < n:
        nl.append(i)
print(nl)

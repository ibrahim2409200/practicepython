n=int(input("Enter Range Number:"))
dl=[]
for i in range(1,n+1):
    if (n%i==0):
        dl.append(i)
print(dl)
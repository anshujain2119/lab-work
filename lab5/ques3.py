c=0
d=0
n= int(input("Enter number: "))
i= int(input("Enter i: "))
while i!=-999:
    if i%n==0:
        d+=1
    else:
        c+=1
    i= int(input("Enter i: "))
print("Divisble",d)
print("Not Divisible",c)
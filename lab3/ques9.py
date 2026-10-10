a1=float(input("Enter a1: "))
b1=float(input("Enter b1: "))
c1=float(input("Enter c1: "))
a2=float(input("Enter a2: "))
b2=float(input("Enter b2: "))
c2=float(input("Enter c2: "))
d=(a1*b2-a2*b1)
if d==0:
    if a1*c2==a2*c1 and b1*c2==b2*c1:
        print("The lines are coincident")
    else:
        print("Lines are parallel")
else:
    print("Intersecting Lines")
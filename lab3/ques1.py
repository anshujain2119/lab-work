import math
x1=float(input("Enter x1: "))
y1=float(input("Enter y1: "))
r=float(input("Enter Radius: "))
x2=float(input("Enter x2: "))
y2=float(input("Enter y2: "))
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
if d<r:
    print("Inside the Boundary")
elif d==r:
    print("On the Boundary")
else:
    print("Outside the Boundary")
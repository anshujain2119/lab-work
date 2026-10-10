s=input("Enter type of shape: ")
if s=="Square":
    side= int(input("Enter side: "))
    a=side**2
elif s=="Rectangle":
    l= int(input("Enter length: "))
    b= int(input("Enter breadth: "))
    a= l*b
elif s=="Circle":
    r= int(input("Enter radius: "))
    a=3.14*r**2
elif s=="Triangle":
    b= int(input("Enter base: "))
    h= int(input("Enter heigth: "))
    a= 0.5*b*h
else: 
    print("Invalid Input")
print(a)
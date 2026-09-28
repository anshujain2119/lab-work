x= float(input("Enter the cost"))
y= float(input("Enter the revenue"))
if x==y:
    print("Break even")
elif y>x:
    print("Profit=",y-x)
else:
    print("lose=",x-y)
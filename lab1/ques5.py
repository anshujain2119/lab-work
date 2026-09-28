x=int(input("Enter x"))
y=int(input("Enter y"))
if x<0 or y<0:
    print("Invalid Input")
else:
    if y%x==0:
        print("Divisible")
    else:
        print("Not Divisible")
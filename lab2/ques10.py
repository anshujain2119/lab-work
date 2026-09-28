p= float(input("Enter no. of pounds of apples"))
c= float(input("Enter amount of cash gain"))
t=p*0.25
if c<t:
    print("You own $",t-c)
else:
    change=c-t
    print("Change = $",change)
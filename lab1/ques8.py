s=int(input("Enter no. of seconds"))
if s<1 or s>86400:
    print("Invalid Input")
else:
    h=s//3600
    h1=s%3600
    m=h1//60
    sec=h1%60
    print(h,":",m,":",sec)
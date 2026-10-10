n=int(input("Enter your number: "))
if n>=10000 and n<=99999:
    a=n//10000
    a1=n%10000
    b=a1//1000
    b1=a1%1000
    c=b1//100
    c1=b1%100
    d=c1//10
    e=c1%10
    if e>=b and e>=c and e>=d and e>=a:
        print("Largest number is",e,"of position 5th")
    elif d>=c and d>=b and d>=a:
        print("Largest number is",d,"of position 4th")
    elif c>=b and c>=a:
        print("Largest number is",c,"of position 3rd")
    elif b>=a:
        print("Largest number is",b,"of position 2nd")
    else:
        print("Largest number is",a,"of position 1st")
else:
    print()
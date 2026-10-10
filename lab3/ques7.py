n=int(input("Enter your number: "))
if n>=100 and n<=999:
    a=n//100
    a1=n%100
    b=a1//10
    c=a1%10
    s=a+b+c
    if n%s==0:
        print(n,"is a Harshad number")
    else:
        print(n,"is not a Harshad number")
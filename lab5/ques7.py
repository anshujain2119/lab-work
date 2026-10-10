n= int(input("Enter: "))
for i in range(n//2):
    if n%i==0:
        print("Not Prime")
    else:
        print("Prime")
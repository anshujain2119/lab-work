x= int(input("Enter x: "))
y= int(input("Enter y: "))
n= int(input("Enter n: "))
for i in range(x+1,y+1):
    if i%n==0:
        print(i,end=" ")
print()
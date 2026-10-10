a1=int(input("Enter a1: "))
a2=int(input("Enter a2: "))
a3=int(input("Enter a3: "))
if a1+a2+a3==180:
    if a1>90 and a2>90 and a3>90:
        print("Acute traiangle")
    elif a1==90 or a2==90 or a3==90:
        print("Right angle triangle")
    elif a1<90 or a2<90 or a3<90:
        print("Obtuse triangle")
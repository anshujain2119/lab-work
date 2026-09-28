c= input("Enter color")
m= input("Enter mode")
if c=="blue":
    if m=="steady":
        print("Clear view")
    else:
        print("Clouds")
elif m=="steady":
    print("Rain")
else:
    print("Snow")
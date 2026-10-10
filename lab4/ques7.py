b= float(input("Enter Budget: "))
s= input("Enter Season(summer/winter): ")

if b<=0 or s not in ["summer","winter"]:
    print("Invalid Input")
else:
    destination=" "
    place=" "
    spent=0.0
    if b<=100:
        destination= "Bulgaria"
        if s=="summer":
            place="Camp"
            spent= b*0.30
        else:
            place="Hotel"
            spent= b*0.70
    elif b<= 1000:
        destination= "Balkans"
        if s=="summer":
            place="Camp"
            spent= b*0.40
        else:
            place="Hotel"
            spent= b*0.80
    else:
        destination="Europe"
        place="Hotel"
        spent= b*0.90
print(f"Somewhere in {destination}")
print(f"{place}-{spent:.2f}")

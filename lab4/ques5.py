n= float(input("Enter distance in Km: "))
p= input("Enter period of day(day/night): ")
if n<0 or p not in ['day','night']:
    print("Invalid Input")
else:
    rate= 37.89 if p=="day" else 43.17
    cheapest= 33.58+(n*rate)
    if n>=20:
        bus_cost= n*4.32
        cheapest= min(cheapest, bus_cost)
    elif n>=100:
        train_cost= n*2.88
        cheapest= min(cheapest, train_cost)
    print(f"{cheapest:.2f}INR")

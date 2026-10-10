h= int(input("Enter no. of holidays: "))
if h<0 or h>365:
    print("Invalid Input")
else:
    workdays=365-h
    play_time=(workdays*63)+(h*127)
    norm=30000
    diff= abs(norm-play_time)
    hours= diff//60
    minutes= diff%60
    if play_time<=norm:
        print("Tom sleeps well")
        print(f"{hours}hours and {minutes}minutes less for play")
    else:
        print("Tom will run away")
        print(f"{hours}hours and {minutes}minutes more for play")
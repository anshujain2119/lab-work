count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
total = 0

while True:
    n = int(input("Enter a number (1-10) or -1 to stop: "))

    if n == -1:
        break

    if n < 1 or n > 10:
        print("Invalid input")
        continue

    total += 1

    if n <= 2:
        count1 += 1
    elif n <= 4:
        count2 += 1
    elif n <= 6:
        count3 += 1
    elif n <= 8:
        count4 += 1
    else:
        count5 += 1

if total == 0:
    print("No valid numbers entered")
else:
    print("1 - 2:", end=" ")
    for i in range(count1):
        print("#", end=" ")
    print(f"{count1 / total * 100:.2f} %")

    print("3 - 4:", end=" ")
    for i in range(count2):
        print("#", end=" ")
    print(f"{count2 / total * 100:.2f} %")

    print("5 - 6:", end=" ")
    for i in range(count3):
        print("#", end=" ")
    print(f"{count3 / total * 100:.2f} %")

    print("7 - 8:", end=" ")
    for i in range(count4):
        print("#", end=" ")
    print(f"{count4 / total * 100:.2f} %")

    print("9 - 10:", end=" ")
    for i in range(count5):
        print("#", end=" ")
    print(f"{count5 / total * 100:.2f} %")

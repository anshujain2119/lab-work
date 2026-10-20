n = int(input("Enter a positive integer N: "))

if n < 1 or n > 1000:
    print("Invalid input")
else:
    slot = 1

    while slot <= 1000:
        if slot % n != 0:
            slot += 1
            continue

        if slot % 4 == 0:
            slot += 1
            continue

        print(slot, end=" ")
        slot += 1

    print()
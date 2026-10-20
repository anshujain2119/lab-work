n = int(input("Enter an odd positive integer: "))

if n <= 0 or n % 2 == 0:
    print("Invalid input")
else:
    m = n // 2

    for i in range(m + 1):
        for j in range(m - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()

    for i in range(m - 1, -1, -1):
        for j in range(m - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()
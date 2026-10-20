n = int(input("Enter the number of lines: "))

if n <= 0:
    print("Invalid input")
else:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for j in range(i):
            print(i, end=" ")
        print()
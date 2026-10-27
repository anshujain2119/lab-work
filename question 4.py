


N = int(input("Enter N: "))
P = int(input("Enter P: "))

if N <= 0 or P <= 0:
    print("Invalid Input")
else:
    result = 1
    count = 0

    while count < P:
        result = result * N
        count += 1

    print("Answer =", result)
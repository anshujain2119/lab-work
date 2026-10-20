n = int(input("Enter a positive integer N: "))

if n < 1:
    print("Invalid input")
else:
    print("Armstrong numbers:")

    num = 1

    while num <= n:
        temp = num
        digits = 0
        
        while temp > 0:
            digits += 1
            temp //= 10

        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10
            power = 1
            i = 0

            while i < digits:
                power *= digit
                i += 1

            total += power
            temp //= 10

        if total == num:
            print(num, end=" ")

        num += 1

    print()


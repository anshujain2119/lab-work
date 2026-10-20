if n <= 0:
    print("Invalid input")
else:
    print("Pattern A:")
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1
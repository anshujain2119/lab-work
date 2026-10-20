numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]

if len(numbers) == 0:
    print("List is empty")
else:
    total = 0
    product = 1
    smallest = numbers[0]

    for num in numbers:
        total += num
        product *= num

        if num < smallest:
            smallest = num

    print("Sum:", total)
    print("Product:", product)
    print("Smallest element:", smallest)

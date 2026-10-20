numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]

n = len(numbers)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Descending order:", end=" ")

for num in numbers:
    print(num, end=" ")

print()

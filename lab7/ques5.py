shift = int(input("Enter shift: "))

small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

for ch in s:
    i = 0

    while i < 26:
        if ch == small[i]:
            result += small[(i + shift) % 26]
            break

        elif ch == capital[i]:
            result += capital[(i + shift) % 26]
            break

        i += 1

print("Encrypted string:", result)
s = input("Enter hyphen-separated words: ")
words = s.split("-")

n = len(words)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if words[j].lower() > words[j + 1].lower():
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

result = "-".join(words)

print(result)

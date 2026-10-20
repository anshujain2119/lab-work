s = input("Enter a sentence: ")
word = input("Enter a word: ")

count = s.count(word)

if word in s:
    print("Word found")
    print("Occurrences:", count)
else:
    print("Word not found")
    print("Occurrences: 0")

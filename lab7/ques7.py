s = input("Enter a string: ")
left = 0
right = len(s) - 1
palindrome = True

while left < right:
    if s[left] != s[right]:
        palindrome = False
        break

    left += 1
    right -= 1

if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")

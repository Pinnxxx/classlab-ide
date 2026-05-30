def is_palindrome(text):
    s = text.lower().replace(" ", "")
    return s == s[::-1]

print("racecar", is_palindrome("racecar"))
print("racecars", is_palindrome("racecars"))
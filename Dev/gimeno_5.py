def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Hello"))
print(is_palindrome("Was it a car or a cat I saw"))
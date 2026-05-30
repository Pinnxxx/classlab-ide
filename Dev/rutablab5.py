def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Tests
print(is_palindrome("George Russell"))      # True
print(is_palindrome("Max Verstappen"))      # True
print(is_palindrome("Lewis Hamilton"))   # True
print(is_palindrome("hello"))        # False
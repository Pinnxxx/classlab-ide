def is_palindrome(text):
    s = text.lower().replace(" ", "")
    return s == s[::-1]
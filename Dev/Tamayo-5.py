def is_palindrome(text):
    s = text.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))                 
print(is_palindrome("Hello"))                  
print(is_palindrome("Was it a car or a cat I saw"))
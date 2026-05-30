import re

def is_palindrome(text):
    s = re.sub(r'[^a-z]', '', text.lower())
    return s == s[::-1]

print(is_palindrome("racecar"))           
print(is_palindrome("Hello"))            
print(is_palindrome("Was it a car or a cat I saw"))
print(is_palindrome("A man, a plan, a canal: Panama"))
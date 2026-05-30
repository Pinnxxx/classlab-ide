def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))                    
print(is_palindrome("Hello"))                      
print(is_palindrome("Was it a car or a cat I saw"))
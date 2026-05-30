def is_palindrome(text):
    reverse = text.replace(" ", "").lower()
    return reverse == reverse[::-1]

print(is_palindrome("madam"))           
print(is_palindrome("python"))          
print(is_palindrome("never odd or even"))  
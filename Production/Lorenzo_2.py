def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))
print(count_vowels("Hello"))      #Test 
print(count_vowels("PROGRAMMING")) 
print(count_vowels("Python"))      
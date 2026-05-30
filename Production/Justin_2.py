def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
print("Hello world = ", count_vowels("Hello World"), "vowels")
print("Progamming = ", count_vowels("Progamming"), "vowels")
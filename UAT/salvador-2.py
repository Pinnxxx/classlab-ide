def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

# Test execution
print(f'"Hello World" -> {count_vowels("Hello World")}')
print(f'"Programming" -> {count_vowels("Programming")}')
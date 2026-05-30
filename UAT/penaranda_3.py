def fizz_buzz():
    for i in range(1, 21):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and not i % 5 == 0:
            print("Fizz")
        elif i % 5 == 0 and not i % 3 == 0:
            print("Buzz")
        else:
            print(i)

print(fizz_buzz())
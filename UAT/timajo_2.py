def div(a, b):
    if a == 0 or b == 0:
        return "Cannot divide by zero"
    return a / b

def add(a, b):
    if a == 0 or b == 0:
        return "Cannot divide by zero"
    return a + b

def sub(a, b):
    if a == 0 or b == 0:
        return "Cannot divide by zero"
    return a - b

def mul(a, b):
    if a == 0 or b == 0:
        return "Cannot divide by zero"
    return a * b

def main():
    a = 10
    b = 4
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))


if __name__ == "__main__":
    main()
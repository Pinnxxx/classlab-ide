def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(add(10, 4))
print(sub(10, 4))
print(mul(10, 4))
print(div(10, 4))
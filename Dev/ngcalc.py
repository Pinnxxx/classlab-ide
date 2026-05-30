def div(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

a = 6
b = 7

print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))
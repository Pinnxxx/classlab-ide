def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if (b == 0):
        return "Cannot divide by 0"
    return a / b

a = 10
b = 4

print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))




def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

a = 10
b = 4

print("Add:", add(a, b))
print("Sub:", sub(a, b))
print("Mul:", mul(a, b))
print("Div:", div(a, b))
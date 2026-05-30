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

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {sub(a, b)}")
print(f"Multiplication: {mul(a, b)}")
print(f"Division: {div(a, b)}")
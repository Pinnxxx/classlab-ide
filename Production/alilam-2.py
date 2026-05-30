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

num1 = 10
num2 = 4

print(num1, "+", num2, " = ", add(num1, num2))
print(num1, "-", num2, " = ", sub(num1, num2))
print(num1, "x", num2, " = ", mul(num1, num2))
print(num1, "/", num2, " = ", div(num1, num2))
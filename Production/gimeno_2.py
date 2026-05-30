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

a, b = map(float, input("Enter two numbers (separated by space): ").split())

print(
    "divide: " + str(div(a, b)) +
    "\nmultiply: " + str(mul(a, b)) +
    "\naddition: " + str(add(a, b)) +
    "\nsubtract: " + str(sub(a, b))
)
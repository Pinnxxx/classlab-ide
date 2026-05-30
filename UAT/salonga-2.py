import random 


def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b


num1 = random.randint(1,5)
num2 = random.randint(0,6)

print( str(num1) + "+" + str(num2) + " = " + str(add(num1,num2)))
print( str(num1) + "-" + str(num2) + " = " + str(sub(num1,num2)))
print( str(num1) + "*" + str(num2) + " = " + str(multiply(num1,num2)))
print( str(num1) + "/" + str(num2) + " = " + str(div(num1,num2)))
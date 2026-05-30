import random

def greetings(name):
    num = random.randint(1,5)
    match num:
        case 1:
            return("Hello " + name + "! Welcome to ClassLab")
        case 2:
            return("Greetings " + name + "! Welcome to ClassLab")
        case 3:
            return("Good Morning " + name + "! Welcome to ClassLab")
        case 4:
            return("Hey there " + name + "! Welcome to ClassLab")
        case 5:
            return("Oh its " + name + "! Welcome to ClassLab")
        case _:
            return("Hello " + name + "! Welcome to ClassLab")

print(greetings("Salonga"))
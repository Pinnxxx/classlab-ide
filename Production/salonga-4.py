import random

def average(nums):
    return sum(nums) / len(nums)


num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
num3 = random.randint(1, 20)
num4 = random.randint(1, 20)

print ("Average of " + str(num1) + " " + str(num2) + " " + str(num3) + " " + str(num4) )
print(average([num1, num2, num3, num4]))
import random

def average(nums):
    return sum(nums) / len(nums)

nums = [random.randint(1, 100) for _ in range(4)]
print("Numbers:", nums)
print("Average:", average(nums))
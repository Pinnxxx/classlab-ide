def average(nums):
    if not nums:
        return "Cannot divide by zero"
    
    return sum(nums) / len(nums)

print(average([12, 8, 20, 16]))
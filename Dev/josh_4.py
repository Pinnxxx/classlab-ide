def average(nums):
    if not nums:
        return "Cannot divide by zero"
    
    return sum(nums) / len(nums)
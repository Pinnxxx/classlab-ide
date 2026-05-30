def average(nums):
    if not nums:
        return "Cannot divide by 0"
    return sum(nums) / len(nums)

print(average([12, 8, 20, 16]))
print(average([]))
print(average([10]))

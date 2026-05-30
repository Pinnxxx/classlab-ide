def average(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

print(average([12, 8, 20, 16]))
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

numbers = [12, 8, 20, 16]
print(average(numbers))
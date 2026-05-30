def average(nums):
    return sum(nums) / len(nums)

def test_average():
    assert average([12, 8, 20, 16]) == 14.0

test_average()
print("Test passed!")
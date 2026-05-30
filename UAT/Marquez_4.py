def largest(a, b, c):
    return max(a, b, c)

# Input numbers
numbers = (420, 999, 123)
test_result = largest(*numbers)
print(f"Test set: {numbers} -> {test_result}")
def largest(a, b, c):
    """Return the largest of three numbers."""
    return max(a, b, c)


if __name__ == "__main__":
    result = largest(4, 9, 2)
    print(f"largest(4, 9, 2) → {result}")
    assert result == 9, f"Test failed: expected 9, got {result}"
    print("Test passed!")
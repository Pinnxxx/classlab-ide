def grade(score):
    # Check parameters
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test cases
test_scores = [75, 50, 99]

# Iterate through the scores and print the results
for current_score in test_scores:
    result = grade(current_score)
    print(f"Grade({current_score}) -> {result}")
def grade(score):
    """Return letter grade based on numeric score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score_input = input("Enter your score: ")
score = float(score_input) 

letter_grade = grade(score)
print(f"Your grade is: {letter_grade}")
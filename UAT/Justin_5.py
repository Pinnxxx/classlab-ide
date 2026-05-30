def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"

print("Grade: 95 =", grade(95))
print("Grade: 74 =", grade(81))
print("Grade: 50 =", grade(74))
print("Grade: 95 =", grade(63))
print("Grade: 95 =", grade(50))
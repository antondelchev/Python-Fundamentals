def grades_as_words(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    if 3 <= grade <= 3.49:
        return "Poor"
    if 3.50 <= grade <= 4.49:
        return "Good"
    if 4.50 <= grade <= 5.49:
        return "Very Good"
    if 5.50 <= grade <= 6.00:
        return "Excellent"


current_grade = float(input())

print(grades_as_words(current_grade))

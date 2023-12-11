student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione": 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grades = {
    91 : "Outstanding",
    81 : "Exceeds Expectations",
    71 : "Acceptable",
    00 : "Fail"
}

for key in student_scores:
    score = student_scores[key]

    for grade in student_grades:
        if score >= grade:
            student_scores[key] = student_grades[grade]
            break

print(student_scores)
    

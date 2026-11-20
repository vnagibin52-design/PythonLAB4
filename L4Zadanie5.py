students = [
    {"name": "Анна", "score": 75, "attempts": 2},
    {"name": "Борис", "score": 58, "attempts": 1},
    {"name": "Виктор", "score": 80, "attempts": 3},
    {"name": "Галина", "score": 60, "attempts": 4},
    {"name": "Дмитрий", "score": 62, "attempts": 3},
    {"name": "Елена", "score": 59, "attempts": 2}
]

list1 = []
for student in students:
    if student["score"] >= 60 and student["attempts"] <= 3:
        list1.append(student["name"])

list2 = [
    student["name"]
    for student in students
    if student["score"] >= 60 and student["attempts"] <= 3
]

print(list1 == list2)
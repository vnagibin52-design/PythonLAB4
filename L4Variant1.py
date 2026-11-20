names = ["Анна", "Борис", "Вера", "Глеб"]
grades = [5, 3, 4, 2]

print("Нумерованная ведомость:")
for i, (name, grade) in enumerate(zip(names, grades), start=1):
    print(f"{i}. {name}: {grade}")

good_students = [name for name, grade in zip(names, grades) if grade >= 4]
print("Студенты с оценкой не ниже 4:", good_students)

students_dict = dict(zip(names, grades))
print("Словарь ФИО → оценка:", students_dict)
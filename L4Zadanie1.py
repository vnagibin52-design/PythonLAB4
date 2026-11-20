list = [5, 2, 3, 5, 4]

counter = 1
for number in list:
    print(f"{counter}. {number}")
    counter += 1

for index, number in enumerate(list, start=1):
    print(f"{index}. {number}")

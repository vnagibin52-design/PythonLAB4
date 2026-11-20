list = []
for i in range(0, 101):
    if i % 2 == 0:
        list.append(i ** 2)

list2 = [i ** 2 for i in range(0, 101) if i % 2 == 0]

print(list == list2)
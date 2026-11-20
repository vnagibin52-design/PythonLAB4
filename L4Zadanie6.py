import time
import statistics

def build_with_loop(data):
    result = []
    for x in data:
        if x % 2 == 0:
            result.append(x * x)
    return result

def build_with_comprehension(data):
    return [x * x for x in data if x % 2 == 0]

sizes = [10000, 100000, 1000000]

for n in sizes:
    data = list(range(n))
    
    loop_times = []
    for i in range(7):
        start = time.time()
        i = build_with_loop(data)
        end = time.time()
        loop_times.append(end - start)
    loop_avg = statistics.mean(loop_times)
    
    listcom_times = []
    for i in range(7):
        start = time.time()
        i = build_with_comprehension(data)
        end = time.time()
        listcom_times.append(end - start)
    listcom_avg = statistics.mean(listcom_times)

    print(f"{n:>8} | {'цикл + append()':<20} |", end = ' ')
    for t in loop_times:
        print(f"{t:.6f}", end = ' ')
    print(f"| {loop_avg:.6f}")

    print(f"{n:>8} | {'list comprehension':<20} |", end = ' ')
    for t in listcom_times:
        print(f"{t:.6f}", end = ' ')
    print(f"| {listcom_avg:.6f}")
    
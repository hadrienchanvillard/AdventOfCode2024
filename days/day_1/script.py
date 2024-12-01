def silver(day: int):
    with open(f"./days/day_{str(day)}/input", "r") as file:
        data = file.read().splitlines()

    res = 0

    list1 = sorted([int(line.split('   ')[0]) for line in data])
    list2 = sorted([int(line.split('   ')[1]) for line in data])

    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])

    return res

def gold(day: int):
    with open(f"./days/day_{str(day)}/input", "r") as file:
        data = file.read().splitlines()

    res = 0

    list1 = sorted([int(line.split('   ')[0]) for line in data])
    list2 = sorted([int(line.split('   ')[1]) for line in data])

    mem = {}
    for num in list2:
        if num not in mem:
            mem[num] = 0
        mem[num] += 1

    for num in list1:
        if num in mem:
            res += num*mem[num]

    return res
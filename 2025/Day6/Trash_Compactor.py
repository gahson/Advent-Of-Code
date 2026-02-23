import math
def part1():
    data = []
    with open("data6.txt", "r", encoding="utf-8") as f:
        for l in f:
            data.append(list(l.strip().split()))
    oper = data[-1]
    data.pop()

    data = [list(map(int, l)) for l in data]
    s = 0
    for i in range(len(oper)):
        if oper[i] == '+':
            for o in range(len(data)):
                s += data[o][i]
        else:
            sp = 1
            for o in range(len(data)):
                sp *= data[o][i]
            s += sp
    return s

def part2():
    data = []
    s = 0
    with open("data6.txt", "r", encoding="utf-8") as f:
        for l in f:
            data.append(l.strip('\n'))
    oper = data[-1]
    data.pop()
    st = 0
    while st < len(oper) - 1:
        i = st + 1
        while oper[i + 1] == ' ':
            i += 1
        nums = []
        for o in range(st, i):
            n = 0
            for op in range(len(data)):
                if data[op][o] != ' ':
                    n *= 10
                    n += int(data[op][o])
            nums.append(n)
        if oper[st] == '+':
            s += sum(nums)
        else:
            s += math.prod(nums)
        st = i + 1
    return s


print(part2())

#print(part1())


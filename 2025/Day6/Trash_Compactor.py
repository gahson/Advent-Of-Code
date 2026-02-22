def part1(data, oper):
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
                


data = []
with open("data6.txt", "r",  encoding="utf-8") as f:
    for l in f:
        data.append(list(l.strip().split()))
oper = data[-1]
data.pop()



data = [list(map(int, l)) for l in data]


print(part1(data, oper))


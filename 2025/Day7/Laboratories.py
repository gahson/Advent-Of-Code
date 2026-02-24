def lab(data):
    streams = set()
    s = 0
    for i, d in enumerate(data[0]):
        if d == 'S':
            streams.add(i)
            break
    for l in data:
        to_add = set()
        to_pop = set()
        for st in streams:
            if l[st] == "^":
                s +=1
                to_add.add(st - 1)
                to_add.add(st + 1)
                to_pop.add(st)
        streams |= to_add
        streams -= to_pop
    return s



data = []
with open("data7.txt", "r", encoding = "utf - 8") as f:
    for l in f:
        data.append(list(l.strip()))
print(lab(data))

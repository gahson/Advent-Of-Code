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

def lab_2(data):
    start_col = 0
    for i, char in enumerate(data[0]):
        if char == 'S':
            start_col = i
            break

    current_paths = {start_col: 1}

    for l in data:
        next_paths = {}
        for col, count in current_paths.items():
            if l[col] == "^":
                next_paths[col - 1] = next_paths.get(col - 1, 0) + count
                next_paths[col + 1] = next_paths.get(col + 1, 0) + count
            else:
                next_paths[col] = next_paths.get(col, 0) + count

        current_paths = next_paths

    return sum(current_paths.values())


data = []
with open("data7.txt", "r", encoding = "utf - 8") as f:
    for l in f:
        data.append(list(l.strip()))
print(lab_2(data))

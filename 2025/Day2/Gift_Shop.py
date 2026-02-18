def gift_shop(data):
    s = 0
    for ran in data:
        for i in range(int(ran[0]), int(ran[1])+1):
            d = str(i)
            size = len(d)

            if d[0] == 0:
                continue
            if size % 2 != 0:
                continue
            print(d[:size//2],"  ",d[size//2:])
            if d[:size//2] == d[size//2:]:
                s += i
    return s




data = []
with open("data2.txt", "r", encoding="utf-8") as f:
    data_t = f.read().split(',')

for d in data_t:
    data.append(d.split('-'))
print(data)
print(gift_shop(data))
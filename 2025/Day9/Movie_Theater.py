def mov_the(data):
    n = len(data)
    max_ar = 0
    for i in range(n):
        for o in range(i+1, n):
            ar = (1 + abs(data[i][0] - data[o][0])) * (1 + abs(data[i][1] - data[o][1]))
            max_ar = max(max_ar, ar)
    return max_ar

data = []
with open("data8.txt", "r", encoding = "utf - 8") as f:
    for l in f:
        data.append(list(map(int, l.strip().split(","))))
print(mov_the(data))
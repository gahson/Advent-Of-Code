def secret_entrance(t):
    k = 0
    x = 50
    for d, v in t:
        if d == 'L':
            x1 = x
            x = x - int(v)
            if x <= 0 and x1 != 0:
                print(d+v)
                k += 1 + abs(x) // 100
            elif x <= 0:
                print(d+v)
                k += abs(x) // 100

        else:
            x = x + int(v)
            if x >= 100:
                print(d + v)
                k += x // 100
        x %= 100

    return k





data = []
with open("data1.txt", "r", encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        dir = l[0]
        val = l[1:]
        data.append([dir, val])

print(secret_entrance(data))

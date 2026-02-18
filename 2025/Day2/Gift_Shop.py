def gift_shop(data):
    s = 0
    for ran in data:
        for i in range(int(ran[0]), int(ran[1])+1):
            d = str(i)
            size = len(d)

            if size % 2 != 0:
                continue
            print(d[:size//2],"  ",d[size//2:])
            if d[:size//2] == d[size//2:]:
                s += i
    return s

def gift_shop2(data):
    s = 0
    for ran in data:
        for i in range(int(ran[0]), int(ran[1])+1):
            d = str(i)
            size = len(d)
            if size < 2:
                continue
            fact = factors(size)

            for f in fact:
                str_splitted = []
                o = 0
                while o * f < size:
                    str_splitted.append(d[o*f:(o+1)*f])
                    o+=1
                if all( x == str_splitted[0] for x in str_splitted):
                    s += i
                    break
    return s

def factors(i):
    fact = [1]
    f = 2
    while f*f <= i:
        if i % f == 0:
            fact.append(f)
            fact.append(i // f)
        f += 1
    return sorted(set(fact), reverse=True)

data = []
with open("data2.txt", "r", encoding="utf-8") as f:
    data_t = f.read().split(',')

for d in data_t:
    data.append(d.split('-'))

print(gift_shop2(data))
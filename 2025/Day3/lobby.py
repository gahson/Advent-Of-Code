def lobby(d):
    s = 0
    for bank in d:

        max_num = bank[0]
        i_max = 0
        for i in range(1, len(bank)-1):
            if bank[i] > max_num:
                max_num = bank[i]
                i_max = i
        s += 10 * max_num
        max_num = 0
        for i in range(i_max + 1, len(bank)):
            if bank[i] > max_num:
                max_num = bank[i]
        s += max_num
    return s

def lobby2(data):
    s = 0
    for bank in data:
        stack = []
        to_rem = len(bank) - 12
        for d in bank:
            while to_rem > 0 and stack and stack[-1] < d:
                stack.pop()
                to_rem -= 1
            stack.append(d)
        stack = stack[:12]
        st = 0
        for num in stack:
            st *= 10
            st += num
        s += st
    return s





data = []
with open('data3.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        digits = [int(n) for n in line]
        data.append(digits)

print(lobby2(data))

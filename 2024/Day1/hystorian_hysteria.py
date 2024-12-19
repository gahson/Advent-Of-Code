from collections import Counter

def hystorian_hysteria1(a, b):
    a = sorted(a)
    b = sorted(b)
    res = 0
    for i in range (len(a)):
        res += abs(a[i] - b[i])
    return res

def hystorian_hysteria2(a, b):
    a2 = [item for item in a if item in b]
    b = dict(Counter(b))
    res = 0
    for i in range (len(a2)):
        res += a2[i] * b[a2[i]]
    return res

a, b = [], []
with open('data.txt', 'r') as file:
    for line in file:  # Iteracja po każdej linii w pliku
        left, right = map(int, line.split())  # Rozdzielanie liczb w linii
        a.append(left)  # Dodawanie liczby po lewej do listy
        b.append(right)  # Dodawanie liczby po prawej do listy

print(hystorian_hysteria1(a,b))
print(hystorian_hysteria2(a,b))
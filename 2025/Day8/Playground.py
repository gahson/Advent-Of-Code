import math
from itertools import combinations


def playg(data):
    edges = []
    for i, j in combinations(range(len(data)), 2):
        p1, p2 = data[i], data[j]
        dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
        edges.append((dist, i, j))

    edges.sort()

    parent = {i: i for i in range(len(data))}
    size = {i: 1 for i in range(len(data))}

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]

    for edge in edges[:1000]:
        union(edge[1], edge[2])

    circuit_sizes = []
    for i in range(len(data)):
        if parent[i] == i:
            circuit_sizes.append(size[i])

    circuit_sizes.sort(reverse=True)

    top_3 = circuit_sizes[:3]

    result = 1
    for s in top_3:
        result *= s

    return result


def playg2(data):
    num_boxes = len(data)
    edges = []

    for i, j in combinations(range(num_boxes), 2):
        p1, p2 = data[i], data[j]
        dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
        edges.append((dist, i, j))

    edges.sort()

    parent = {i: i for i in range(num_boxes)}
    size = {i: 1 for i in range(num_boxes)}

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    for edge in edges:
        dist, i, j = edge

        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]

            if size[root_i] == num_boxes:
                x1 = data[i][0]
                x2 = data[j][0]
                return x1 * x2



data = []
with open("data8.txt", "r", encoding="utf-8") as f:
    for l in f:
        l = list(map(int, l.strip().split(",")))
        data.append(l)

print(playg2(data))

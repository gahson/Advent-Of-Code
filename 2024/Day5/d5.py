from collections import defaultdict
rules = []
pages = []
with open('data.txt', 'r') as file:
    filelines = file.readlines()

for i in range(len(filelines)):
    
    if filelines[i] == '\n':
        idx = i+1
        break
    l, r = map(int, filelines[i].split('|'))
    rules.append([l,r]) 

for i in range(idx, len(filelines)):
    pages.append(list(map(int, filelines[i].split(','))))

rule_list = defaultdict(list)
for lr, rr in rules:
    rule_list[lr].append(rr)

res = 0
pages2 = []
for page in pages:
    bef =[ page[0]]
    n = len(page)
    for i in range(1,n):
        for b in bef:
            if b in rule_list[page[i]]:
                if page not in pages2:
                    pages2.append(page)
                break
        else:
            bef.append(page[i])
    if len(bef) == n:
        res += page[n//2]
    

print(res)

# second star excersise
res2 = 0
def topological_sort(graph, upd):
    visited = set()
    restored_page = []

    def dfs(node):
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                dfs(n)
        restored_page.append(node)
    
    for u in upd:
        if u not in visited:
            dfs(u)

    return restored_page[::-1]

for page in pages2:
    rule_list = defaultdict(list) 
    
    for lr, rr in rules:
        if lr in page and rr in page:
            
            rule_list[lr].append(rr)
    
    sorted_page = topological_sort(rule_list, page)
    res2 += sorted_page[len(sorted_page)//2]

            
print(res2)
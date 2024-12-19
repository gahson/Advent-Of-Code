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

rule_list = [[]for i in range(100)]
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
                pages2.append(page)
                break
        else:
            bef.append(page[i])
    if len(bef) == n:
        res += page[n//2]

print(res)

# second star excersise

for page in pages2:
    pass
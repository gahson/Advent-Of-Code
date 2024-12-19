import re

with open('data.txt', 'r') as file:
    input = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

instructions = re.findall(pattern, input)
ins = [[int(x), int(y)] for x, y in instructions]
res = 0
for x, y in ins:
    res += x * y
#print(res)
pattern2 = r"don't\(\).*?(?=do\(\)|$)"


with open('data.txt', 'r') as file:
    input = file.read()
input = re.sub(pattern2, 'XXXXX', input, flags=re.DOTALL)

#print(input)

instructions2 = re.findall(pattern, input)
ins = [[int(x), int(y)] for x, y in instructions2]
res = 0
for x, y in ins:
    res += x * y
print(res)


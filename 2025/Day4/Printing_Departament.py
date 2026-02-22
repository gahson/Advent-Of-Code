def part1(data):
    s = 0
    rows = len(data)
    cols = len(data[0])
    neighbours = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                curr_nei = 0
                for rn, cn in neighbours:
                    cr, cc = r + rn, c + cn
                    if 0 <= cr < rows and 0 <= cc < cols and data[cr][cc] == '@':
                        curr_nei += 1
                if curr_nei < 4:
                    s += 1
    return s

def part2(data):
    s_fin = 0
    rows = len(data)
    cols = len(data[0])
    neighbours = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    
    while True:
        s = 0
        to_remove = [] 
        
        for r in range(rows):
            for c in range(cols):
                if data[r][c] == '@':
                    curr_nei = 0
                    for rn, cn in neighbours:
                        cr, cc = r + rn, c + cn
                        if 0 <= cr < rows and 0 <= cc < cols and data[cr][cc] == '@':
                            curr_nei += 1
                    if curr_nei < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
            
        for r, c in to_remove:
            if data[r][c] == '@': 
                data[r][c] = '.'
                s += 1
        s_fin += s
        
    return s_fin


with open('data4.txt', 'r') as f:
    grid = [list(line.strip()) for line in f if line.strip()]



print(part2(grid))

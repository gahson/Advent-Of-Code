def cafeteria(merged_ranges, ids):
    s = 0
    n = len(merged_ranges)
    
    for person_id in ids:
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            start, end = merged_ranges[mid]
            
            if start <= person_id <= end:
                s += 1
                break
            elif person_id < start:
                high = mid - 1
            else:
                low = mid + 1
                
    return s

def cafeteria_2(merged_ranges):
    s = 0
    for r in merged_ranges:
        s += r[1] - r[0] + 1
    return s

def find_max_range(ranges):

    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)

    return merged








with open("data5.txt", "r",  encoding="utf-8") as f:
    ranges, ids = f.read().strip().split("\n\n")
    ranges = ranges.split("\n")
    ranges = [list(map(int, r.split("-"))) for r in ranges]
    ids = list(map(int, ids.split("\n")))

ranges = find_max_range(ranges)

print(cafeteria(ranges, ids))
print(cafeteria_2(ranges))


def count_safe2(rep):#brute force hehe
    
    for i in range(1, len(rep)):
        new_list = rep[:]
        new_list[i-1] += new_list.pop(i)
        if is_safe(new_list) == 1:
            return 1
    new_list = rep[:]
    new_list.pop(0)
    if is_safe(new_list) == 1:
            return 1
    new_list = rep[:]
    new_list.pop(len(rep)-1)
    if is_safe(new_list) == 1:
            return 1
    return 0


def count_safe(D):
    safe = 0
    safe2 = 0
    for rep in D:
        if is_safe(rep):
            safe += 1
        else:
            safe2 += count_safe2(rep)

    return safe, safe + safe2

def is_safe(rep):
    if rep[0] > 0:
            inc = 1
    else: 
        inc = -1
    for i in range(len(rep)):
        if rep[i] * inc < 1 or rep[i] * inc > 3:
                
            return 0
    else:
        return 1
    


def refactor(D):
    D_refactored = []
    for rep in D:
        rep_ref = []
        for i in range(len(rep) - 1):
            rep_ref.append(rep[i+1] - rep[i])
        D_refactored.append(rep_ref)
    return D_refactored

        


D = []
with open('data.txt', 'r') as file:
    for line in file:  # Iteracja po każdej linii w pliku
       D.append(list(map(int, line.split())))
'''D = [[7, 6, 4 ,2, 1],
[1 ,2, 7 ,8, 9],
[9, 7 ,6, 2, 1],
[1 ,3 ,2 ,4 ,5],
[8, 6, 4, 4, 1],
[1 ,3 ,6, 7 ,9]]'''
D = refactor(D)
print(count_safe(D))


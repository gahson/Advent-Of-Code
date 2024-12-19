def create5l_v_h_d_words(T):
    #horizontal
    N = len(T)
    n = len(T[0])
    words = []
    #horizontal
    for line in T:
        for i in range(n - 3):
            word = line[i:i+4]
            words.append(word)
            words.append(word[::-1])
    #vertical
    for i in range(n):
        for o in range(N-3):
            word = ''
            for l in range(4):
                word += T[o+l][i]
            words.append(word)
            words.append(word[::-1])
    #diagonal
    for i in range(N-3):
        for o in range(n-3):
            word1 = ''
            word2 = ''
            for l in range(4):
                word1 += T[i+l][o+l]
                word2 += T[i+l][o+3-l]
            words.append(word1)
            words.append(word1[::-1])
            words.append(word2)
            words.append(word2[::-1])

    return words


def xshape_mas(T):
    #horizontal
    N = len(T)
    n = len(T[0])
    
    res = 0
    #diagonal
    for i in range(N-2):
        for o in range(n-2):
            word1 = ''
            word2 = ''
            for l in range(3):
                word1 += T[i+l][o+l]
                word2 += T[i+l][o+2-l]
            if (word1 == "MAS" or word1[::-1] =="MAS" ) and  (word2 == "MAS" or word2[::-1] =="MAS" ) :
                res += 1        

    return res    

input = []
with open ('data.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

words = create5l_v_h_d_words(input)

res = 0
for word in words:
    if word == "XMAS":
        res += 1

print(res)

print(xshape_mas(input))
    

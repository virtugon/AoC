with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0
m = len(lines)
n = len(lines[0])

def search_diag(x, y):
    word_count = 0
    word = []
    if y-1 >= 0 and x-1 >=0 and y+1 < m and x+1 < n:
        word.append(lines[y-1][x-1])
        word.append(lines[y][x])
        word.append(lines[y+1][x+1])
    
        if ''.join(word) == "MAS" or ''.join(word) == "SAM":   
            word.clear()
            word.append(lines[y+1][x-1])
            word.append(lines[y][x])
            word.append(lines[y-1][x+1])
            if ''.join(word) == "MAS" or ''.join(word) == "SAM": 
                word_count+=1

    return word_count

for i in range(m):
    for j in range(n):
        if lines[i][j] == "A":
            res+=search_diag(j, i)
        j+=1
    i+=1

print(res)
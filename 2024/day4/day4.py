with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0
m = len(lines)
n = len(lines[0])

# Simplified my thought process by splitting the search into seperate functions.
def search_horizontal(x, y):
    word_count = 0
    if lines[y][x-3:x+1] == "SAMX":
        word_count+=1
    if lines[y][x:x+4] == "XMAS":
        word_count+=1
    return word_count

def search_vertical(x, y):
    word_count = 0
    word = []
    if y-3 >= 0:
        for i in range(0,4):
            word.append(lines[y-i][x])
        if ''.join(word) == "XMAS":
            word_count+=1
    word.clear()
    if y+3 < m:
        for i in range(0,4):
            word.append(lines[y+i][x])
        if ''.join(word) == "XMAS":
            word_count+=1
    return word_count

def search_diag(x, y):
    word_count = 0
    word = []
    for i in range(0,4):
        j=i
        if y-j >= 0 and x-i >= 0:
            word.append(lines[y-j][x-j])
        else:
            break
        if ''.join(word) == "XMAS":
            word_count+=1
 
    word.clear()
    for i in range(0,4):
        if y-i >= 0 and x+i < n:
            word.append(lines[y-i][x+i])
        else:
            break
        if ''.join(word) == "XMAS":
            word_count+=1

    word.clear()
    for i in range(0,4):
        j=i
        if y+i < m and x+i < n:
            word.append(lines[y+i][x+i])
        else:
            break
        if ''.join(word) == "XMAS":
            word_count+=1

    word.clear()
    for i in range(0,4):
        j=i
        if y+i < m and x-i >= 0 < n:
            word.append(lines[y+i][x-i])
        else:
            break
        if ''.join(word) == "XMAS":
            word_count+=1
    return word_count

for i in range(m):
    for j in range(n):
        if lines[i][j] == "X":
            res+=search_horizontal(j, i)
            res+=search_vertical(j, i)
            res+=search_diag(j, i)
        j+=1
    i+=1

print(res)
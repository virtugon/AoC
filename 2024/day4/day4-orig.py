with open("inputcal.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0
m = len(lines)
n = len(lines[0])

def find_word(x, y):
    word = "XMAS"
    word_count = 0
    yc = 0
    for yd in range(-1,2):
        xc = 0
        for xd in range(-1,2):
            word_index = 0
            while word_index < len(word):
                ca = xd*xc
                print(ca)
                cb = yd*yc
                print(cb)
                if ca == 0 and cb == 0:
                    next
                if 0 < x+ca > m-1 or 0 < y+cb > n-1:
                    print(f"Index stop op {x}+{ca} en {y}+{cb}")
                    break
                print(f"Working on {x+ca},{y+cb}:")
                print(lines[x+ca][y+cb])
                print(word[word_index])
                if lines[x+ca][y+cb] == word[word_index]:
                    if word_index == len(word)-1:
                        print("Yay!")
                        word_count+=1
                        break
                    word_index+=1
                    xc+=1
                else:
                    print("Breaking")
                    break
            xd+=1
        yc+=1
        yd+=1
    return word_count

for i in range(m):
    for j in range(n):
        if lines[i][j] == "X":
            print(f"===== X op {i},{j} =======")
            res+=find_word(i,j)
        j+=1
    i+=1

print(res)
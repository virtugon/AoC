with open("input.txt") as fo:
    lines = fo.readlines()

totalScore = 0

for line in lines:
    blub = line.rstrip().split("|")
    winNum = blub[0].split(":")
    winNum = winNum[1].strip().split(" ")
    winNum = list(filter(None, winNum))
    ownNum = blub[1].strip().split(" ")
    ownNum = list(filter(None, ownNum))

    numWin = 0
   
    for i in winNum:
        for j in ownNum:
            if j == i:
                numWin*=2
                if numWin == 0:
                    numWin = 1
    totalScore+=numWin
print(totalScore)

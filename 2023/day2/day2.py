maxRed = 12
maxGreen = 13
maxBlue = 14

gameList = {}
gameNumList = []
with open("input.txt") as fo:
    for line in fo:
        addGame = True
        gameNum = line[0:line.index(':')]
        gameLine = line[line.index(':')+1:].split(';')
        for item in gameLine:
            hand = item.split(',')
            for stone in hand:
                stoneCount = {'red':0,'green':0,'blue':0}
                stoneThingy = stone.strip().split(' ')
                stoneCount[stoneThingy[1]]+=int(stoneThingy[0].strip())
                if stoneCount['red'] > maxRed or stoneCount['green'] > maxGreen or stoneCount['blue'] > maxBlue:
                    addGame = False

        if addGame:        
            gameNumList.append(int(gameNum.split(' ')[1]))
        
print(sum(gameNumList))
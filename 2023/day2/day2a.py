powerList = []

with open("input.txt") as fo:
    for line in fo:
        gameNum = line[0:line.index(':')]
        gameLine = line[line.index(':')+1:].split(';')
        stoneCount = {'red':0,'green':0,'blue':0}
        for item in gameLine:
            hand = item.split(',')
            for stone in hand:
                stoneThingy = stone.strip().split(' ')
                if stoneCount[stoneThingy[1]]<int(stoneThingy[0].strip()):
                    stoneCount[stoneThingy[1]]=int(stoneThingy[0].strip())
        powerList.append(stoneCount['red']*stoneCount['green']*stoneCount['blue'])

print(sum(powerList))
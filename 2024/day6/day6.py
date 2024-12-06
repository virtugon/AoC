with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Find starting position
pos = [0, 0]
for i in range(len(lines)):
    try:
        pi = lines[i].index("^")
        if pi > -1:
            pos = [pi, i] # X, Y on a grid
            break
    except:
        continue

# Start walking
direction = "up"
max_width = len(lines[0])-1
max_height = len(lines)-1
newpos = [0, 0]
poslist = [pos]
while True:
    match direction:
        case "up":
            newpos = [pos[0], pos[1]-1]
        case "down":
            newpos = [pos[0], pos[1]+1]
        case "left":
            newpos = [pos[0]-1, pos[1]]
        case "right":
            newpos = [pos[0]+1, pos[1]]

    x, y = newpos
    if x > max_width or x <0 or y > max_height or y < 0:
        break
    elif lines[y][x] == "#":
        match direction:
            case "up":
                direction = "right"
            case "down":
                direction = "left"
            case "left":
                direction = "up"
            case "right":
                direction = "down"
    else:
        pos = newpos
        if pos not in poslist:
            poslist.append(pos)

print(len(poslist))
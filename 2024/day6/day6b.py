with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def get_next_position(x, y, direction):
    match direction:
        case "up":
            newpos = [x, y-1]
        case "down":
            newpos = [x, y+1]
        case "left":
            newpos = [x-1, y]
        case "right":
            newpos = [x+1, y]
    return newpos

def get_new_direction(direction):
    match direction:
            case "up":
                direction = "right"
            case "down":
                direction = "left"
            case "left":
                direction = "up"
            case "right":
                direction = "down"
    return direction

def walk(pos, direction, max_width, max_height):
    err = False
    newpos = get_next_position(pos[0], pos[1], direction)
    x, y = newpos
    if x > max_width or x < 0 or y > max_height or y < 0:
        err = True
    elif lines[y][x] == "#":
        direction = get_new_direction(direction)
    else:
        pos = newpos
    return pos, direction, err

def check_possible_loops(pos, direction, max_width, max_height):
    startpos = pos
    startdirection = direction
    x, y = pos
    #tmppos = get_next_position(x, y, direction)
    #x1, y1 = tmppos
    #if x1 < max_width and x1 >= 0 and y1 < max_height and y1 >= 0:
    #    if lines[y1][x1] == "#":
    #        return 0
    direction = get_new_direction(direction)
    safety_switch = 0
    while x < max_width and x >= 0 and y < max_height and y >= 0 and safety_switch < 20000:
        safety_switch+=1
        pos, direction, err = walk(pos, direction, max_width, max_height)
        if err:
            break
        if pos == startpos and direction == startdirection:
            #print(safety_switch)
            return 1
        x, y = pos
    return 0

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
loop_count = 0
while True:
    loop_count += check_possible_loops(pos, direction, max_width, max_height)
    pos, direction, err = walk(pos, direction, max_width, max_height)
    if err:
        break
    if pos not in poslist:
        poslist.append(pos)

print(len(poslist))
print(loop_count)
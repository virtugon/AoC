with open("input.txt") as file:
    lines = file.readlines()

safeReports = 0
for line in lines:
    reports = list(map(int, line.rstrip().split(" ")))
    safe = False
    direction = 0 # 0 = unset, 1 = increasing, 2 = decreasing
    dampener = False
    for i in range(len(reports)-1):
        inc = 1
        if direction == 0:
            if int(reports[0]) < int(reports[len(reports)-1]):
                direction = 1
            else:
                direction = 2

        # Logic for part 2
        if abs(reports[i]-reports[i+1]) > 3 and not dampener:
            if i < len(reports)-2:
                inc = 2
            dampener = True
            
        if (direction == 1 and reports[i] > reports[i+1]) or (direction == 2 and reports[i] < reports[i+1]) or reports[i] == reports[i+1] and not dampener:
            if i < len(reports)-2:
                inc = 2
            dampener = True

        # Process line
        if abs(reports[i]-reports[i+inc]) < 4:
            if (direction == 1 and reports[i] < reports[i+inc]):
                safe = True
            elif (direction == 2 and reports[i] > reports[i+inc]):
                safe = True
            else:
                safe = False
                break
        else:
            safe = False
            break
    
    if safe:
        safeReports += 1

print(safeReports)
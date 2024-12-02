# Do-over of day 2 part 2 because I wanted to take another approach but not destroy my first attempt :)
with open("input.txt") as file:
    lines = file.readlines()

def checkList(reports):
    safe = True
    for i in range(len(reports)-1):
        if not 1<=(abs(reports[i]-reports[i+1]))<=3:
            safe = False
    if not (reports==sorted(reports) or reports==sorted(reports,reverse=True)):
        safe = False
    return safe

safeReports = 0
safeDampener = 0
for line in lines:
    # Part 1
    reports = list(map(int, line.rstrip().split(" ")))
    if checkList(reports):
        safeReports+=1

    # Part 2
    ok = False
    for j in range(len(reports)):
        r = reports[:j] + reports[j+1:]
        if checkList(r):
            ok = True
    if ok:
        safeDampener += 1

print(safeReports)
print(safeDampener)
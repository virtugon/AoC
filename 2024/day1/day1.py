with open("input.txt") as file:
    lines = file.readlines()

left = []
right = []
diff = 0

for line in lines:
    line = line.rstrip().split("   ")
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

#  Part 1 (optimized version)
for l, r in zip(left, right):
    diff += abs(l - r)

# Part 2
totalScore = []
for i in left:
    ctr = 0
    for j in right:
        if j == i:
            ctr += 1
    totalScore.append(i*ctr)

print(diff)
print(sum(totalScore))
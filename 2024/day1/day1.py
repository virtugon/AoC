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
    
for i in range(len(left)):
    if left[i] > right[i]:
        diff += left[i] - right[i]
    else:
        diff += right[i] - left[i]

print(diff)
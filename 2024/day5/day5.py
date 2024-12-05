with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

ordering_rules = []
page_numbers = []
correct_updates = []
middle_numbers = []

# Split input into two lists.
for line in lines:
    if not line.find("|") == -1:
        ordering_rules.append(line.split("|"))
    elif not line.find(",") == -1:
        page_numbers.append(line.split(","))
    else:
        next

# Match all rules against all lines and collect the correct lines in a list.
for i in range(len(page_numbers)):
    update_status = 0
    for j,h in ordering_rules:
        try:
            a = page_numbers[i].index(j)
            b = page_numbers[i].index(h)
            if a < b:
                update_status += 1
        except:
            update_status += 1
    if update_status == len(ordering_rules):
        correct_updates.append(i)

# Find the middle page number
for i in range(len(correct_updates)):
    j = len(page_numbers[correct_updates[i]])//2
    middle_numbers.append(page_numbers[correct_updates[i]][j])

middle_numbers = list(map(int, middle_numbers))
print(sum(middle_numbers))
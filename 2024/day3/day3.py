import re

with open("input.txt") as file:
    input = file.read()

# Somebody told me I should be using snake case variable names, so I'm trying to comply :)
#se = r"mul\(\d{1,3}\,\d{1,3}\)" # RegExp for part 1
se = r"(do\(\)|don't\(\)|mul\(\d{1,3}\,\d{1,3}\))" # RegExp for part 2
memory_fragments = re.findall(se, input)
mulval = 0
do_exec = True

for fragment in memory_fragments:
    if fragment == "do()":
        do_exec = True
    elif fragment == "don't()":
        do_exec = False

    if do_exec and fragment[:3] == "mul":
        comma = fragment.find(",")
        mulval += int(fragment[4:comma])*int(fragment[comma+1:-1])

print(mulval)
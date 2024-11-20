lines = []
numbers = []
with open("input.txt") as fo:
    for line in fo:
        row = []
        for char in line:
            row.append(char.strip())
        lines.append(row)

for row in enumerate(lines):
    print(f"== Row {row[0]} ==")
    for char in enumerate(row[1]):
        procChar = False
        print(f"column {char[0]}")
        # If the character is a digit, then begin testing if it's adjacent to a symbol.
        if char[1].isdigit():
            # Check only if in bounds of array
            if row[0] >= 0 and char[0]-1 >= 0 and char[0] < len(lines[row[0]]):
                # Check horizontal connections
                if lines[row[0]][char[0]-1] != '.' and not lines[row[0]][char[0]-1].isdigit():
                    print("Match links!")
                    procChar = True
                if lines[row[0]][char[0]+1] != '.' and not lines[row[0]][char[0]+1].isdigit():
                    print("Match rechts!")
                    procChar = True

                #check vertically
                if lines[row[0]-1][char[0]] != '.' and not lines[row[0]-1][char[0]].isdigit():
                    print("Match onder!")
                    procChar = True
                if row[0]+1 < len(lines) and lines[row[0]+1][char[0]] != '.' and not lines[row[0]+1][char[0]].isdigit():
                    print("Match boven!")
                    procChar = True

                # Check diagonally
                if lines[row[0]-1][char[0]-1] != '.' and not lines[row[0]-1][char[0]-1].isdigit():
                    print("Match linksonder")
                    procChar = True
                if row[0]+1 < len(lines) and lines[row[0]+1][char[0]-1] != '.' and not lines[row[0]+1][char[0]-1].isdigit():
                    print("Match linksboven")
                    procChar = True
                if lines[row[0]-1][char[0]+1] != '.' and not lines[row[0]-1][char[0]+1].isdigit():
                    print("Match rechtsonder")
                    procChar = True
                if row[0]+1 < len(lines) and lines[row[0]+1][char[0]+1] != '.' and not lines[row[0]+1][char[0]+1].isdigit():
                    print("Match rechtsboven")
                    procChar = True

            # if a digit has a connection with a symbol, get the full digit from the row.
            if procChar:
                numChar = lines[row[0]][char[0]]
                # Add digits to the left
                for i in range(char[0] - 1, -1, -1):
                    if lines[row[0]][i].isdigit():
                        numChar = lines[row[0]][i] + numChar
                    else:
                        break
                # Add digits to the right
                for i in range(char[0] +1, len(lines[row[0]])):
                    if lines[row[0]][i].isdigit():
                        numChar = numChar + lines[row[0]][i]
                    else:
                        break
                if len(numbers)<1 or numbers[-1] != int(numChar):
                    numbers.append(int(numChar))

print(numbers)
print(sum(numbers))
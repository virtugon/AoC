import re

def convertNum(num):
  match num:
    case 'one':
      return 1
    case 'two':
      return 2
    case 'three':
      return 3
    case 'four':
      return 4
    case 'five':
      return 5
    case 'six':
      return 6
    case 'seven':
      return 7
    case 'eight':
      return 8
    case 'nine':
      return 9
    case 'zero':
      return 0

num = []
numstring = 'one|two|three|four|five|six|seven|eight|nine|zero'
restring = r'(\d|' + numstring + ')'
revstring = r'(\d|' + numstring[::-1] + ')'
with open("input.txt", "r") as fo:
  for line in fo:
    fc = re.search(restring, line).group()
    if not fc.isdigit():
      fc = convertNum(fc)
    lc = re.search(revstring, line[::-1]).group()
    if not lc.isdigit():
      lc = convertNum(lc[::-1])
    num.append(int(f"{fc}{lc}"))
print(sum(num))
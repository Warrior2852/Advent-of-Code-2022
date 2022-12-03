from itertools import islice

file = open('day3.txt', 'r')
total = 0
while True:
    lines = list(islice(file, 3))
    if lines == []:
        break
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    chars1 = chars = [char for char in lines[0]]
    chars2 = chars = [char for char in lines[1]]
    chars3 = chars = [char for char in lines[2]]
    commonList = list(set(chars1).intersection(list(set(chars2).intersection(chars3))))
    common = commonList[0]
    commonAscii = ord(common)
    if commonAscii < 91:
        priority = commonAscii - 38
    else:
        priority = commonAscii - 96
    total += priority
print(total)
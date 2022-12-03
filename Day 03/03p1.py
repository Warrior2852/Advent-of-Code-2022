file = open('day3.txt', 'r')
lines = file.readlines()
total = 0
for line in lines:
    line = line.strip()
    chars = [char for char in line]
    halfsize = len(chars) // 2
    chars1 = chars[:halfsize]
    chars2 = chars[halfsize:]
    commonList = list(set(chars1).intersection(chars2))
    common = commonList[0]
    commonAscii = ord(common)
    if commonAscii < 91:
        priority = commonAscii - 38
    else:
        priority = commonAscii - 96
    total += priority
print(total)
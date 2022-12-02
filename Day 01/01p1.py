file = open('day1.txt', 'r')
lines = file.readlines()
count = 0
counter = 0
max = 0
for line in lines:
    counter = counter + 1
    line = line.strip()
    if line == "" or counter == len(lines):
        if count > max:
            max = count
        count = 0
        continue
    intLine = int(line)
    count = count + intLine
print(max)
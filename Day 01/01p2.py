file = open('day1.txt', 'r')
lines = file.readlines()
count = 0
counter = 0
first = 0
second = 0
third = 0
for line in lines:
    counter = counter + 1
    line.strip()
    if line == "\n" or counter == len(lines):
        if count > first:
            third = second
            second = first
            first = count
        elif count > second:
            third = second
            second = count
        elif count > third:
            third = count
        count = 0
        continue
    intLine = int(line)
    count = count + intLine
total = first + second + third
print(total)
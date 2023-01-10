file = open('day6.txt', 'r')
lines = file.readlines()
count = 1
last = []
for line in lines:
    line = line.strip()
    chars = [char for char in line]
    for i in range(0, len(chars)):
        if len(last) == 14:
            last.pop(0)
        last.append(chars[i])
        if len(last) == 14:
            if len(set(last)) == len(last):
                print(set(last))
                break
        count += 1
print(count)
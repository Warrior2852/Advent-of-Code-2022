file = open('day4.txt', 'r')
lines = file.readlines()
count = 0
for line in lines:
    line = line.strip()
    split = line.split(",")
    left = split[0].split("-")
    right = split[1].split("-")
    if ((int(left[0]) >= int(right[0])) and (int(left[1]) <= int(right[1]))) or ((int(left[0]) <= int(right[0])) and (int(left[1]) >= int(right[1]))):
        count += 1
print(count)
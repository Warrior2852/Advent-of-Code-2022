file = open('day2.txt', 'r')
lines = file.readlines()
score = 0
for line in lines:
    line = line.strip()
    chars = [char for char in line]
    if chars[2] == "X":
        if chars[0] == "A":
            score += 3
        elif chars[0] == "B":
            score += 1
        elif chars[0] == "C":
            score += 2
    elif chars[2] == "Y":
        if chars[0] == "A":
            score += 4
        elif chars[0] == "B":
            score += 5
        elif chars[0] == "C":
            score += 6
    elif chars[2] == "Z":
        if chars[0] == "A":
            score += 8
        elif chars[0] == "B":
            score += 9
        elif chars[0] == "C":
            score += 7
print(score)
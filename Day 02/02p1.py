file = open('day2.txt', 'r')
lines = file.readlines()
score = 0
for line in lines:
    line = line.strip()
    chars = [char for char in line]
    if chars[2] == "X":
        score += 1
        if chars[0] == "A":
            score += 3
        elif chars[0] == "C":
            score += 6
    elif chars[2] == "Y":
        score += 2
        if chars[0] == "A":
            score += 6
        elif chars[0] == "B":
            score += 3
    elif chars[2] == "Z":
        score += 3
        if chars[0] == "B":
            score += 6
        elif chars[0] == "C":
            score += 3
print(score)
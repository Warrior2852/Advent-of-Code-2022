file = open('day5.txt', 'r')
lines = file.readlines()
ready = 0
grid = [["N","C","R","T","M","Z","P"],["D","N","T","S","B","Z"],["M","H","Q","R","F","C","T","G"],["G","R","Z"],["Z","N","R","H"],["F","H","S","W","P","Z","L","D"],["W","D","Z","R","C","G","M"],["S","J","F","L","H","W","Z","Q"],["S","Q","P","W","N"]]
for line in lines:
    if line == "\n":
        ready = 1
        continue
    if ready == 0:
        continue
    line = line.strip()
    instruct = line.split(" ")
    num = int(instruct[1])
    origin = (int(instruct[3]))-1
    to = (int(instruct[5]))-1
    buffer = []
    for i in range(0, num):
        buffer.append(grid[origin].pop())
    grid[to].extend(buffer)
ans = ""
for j in range(0, len(grid)):
    ans = ans + grid[j][-1]
print(ans)
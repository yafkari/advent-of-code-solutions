nbs: list = []
ans: int = -1
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        nbs.append(int(line))

for i in range(len(nbs)):
    if ans != -1:
        break
    for j in range(len(nbs)):
        if nbs[i]+nbs[j] == 2020:
            ans = nbs[i]*nbs[j]
            break
print(ans)

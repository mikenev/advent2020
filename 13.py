#!/usr/bin/python3

filename = "13.input"
rd = open(filename, "r")

canDepart = int(rd.readline().strip())
line = rd.readline().strip().split(",")

minTime = -1
result = 0
maxStep = 0
maxIdx = 0
d = {}
idx = -1

for i in line:
    idx += 1
    if i == "x":
        continue
    busId = int(i)
    diff = canDepart % busId
    diff = busId - diff

    if busId > maxStep:
        maxStep = busId
        maxIdx = idx
    d[busId] = idx

    if minTime == -1 or diff < minTime:
        minTime = diff
        result = minTime * busId


print(result)

print(d)

idx = 700000000000263
idx = 760171380521445 + maxIdx # 939 minutes to calculate on Azure instance
cnt = 0
while True:
    found = True
    cnt += 1
    if cnt % 1000000 == 0:
        print(idx)
    #print(idx)

    for i in d:
        if (idx + d[i] - maxIdx) % i != 0:
            found = False
            break

    if found:
        print(idx - maxIdx)
        break

    idx += maxStep

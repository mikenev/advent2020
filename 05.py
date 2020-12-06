#!/bin/python3

rd = open("05.input", "r")

maxId = 0
ids = []

while True:
    line = rd.readline().strip()
    low = 0
    high = 127
    row = 0

    if not line:
        break;

    for i in range(0,6):
        mid = low + int((high-low)/2)
        if line[i] == "F":
            high = mid
        else:
            low = mid+1
        #print(line[i], " low=", low, " high=", high)

    if line[6] == "F":
        row = low
    else:
        row = high

    low = 0
    high = 7
    seat = 0

    for i in range(7,9):
        mid = low + int((high-low)/2)
        if line[i] == "L":
            high = mid
        else:
            low = mid+1
    
    if line[9] == "L":
        seat = low
    else:
        seat = high
    
    id = row * 8 + seat
    ids.append(id)
    #ids.insert(id)
    #print ("row=", row, " seat=", seat, " id=", id)

    if id > maxId:
        maxId = id

print(maxId)

ids.sort()
#print(ids)
for i in range(0, len(ids)-1):
    if ids[i] != ids[i+1] -1:
        print(ids[i]+1)
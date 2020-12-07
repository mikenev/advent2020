#!/bin/python3

def DFS(map, seen, current):
    if "shiny gold bag" in map[current]:
        seen[current] = True
    
    if current in seen and seen[current] == True:
        return True

    for key in map[current]:
        if DFS(map, seen, key):
            seen[current] = True
            return True
    
    return False

def DFS2(map, current, ans, factor):
    #print (factor, current)
    subBags = map[current];

    for key in subBags.keys():
     #   print(key, ":", subBags[key])
        ans["ans"] += factor * subBags[key]
        DFS2(map, key, ans, factor * subBags[key])
    return

rd = open("07.input", "r")

map = {}

while True:
    line = rd.readline().strip(" .\n")

    if not line:
        break

    parts = line.replace("bags", "bag").split(" contain ")
    key = parts[0]
    
    map[key] = {}

    if parts[1] == "no other bag":
        continue

    contains = parts[1].split(", ")

    for subBag in contains:
        parts = subBag.split(" ", 1)
        count = int(parts[0])
        bag = parts[1]
        map[key].update({bag: count})


#part 1
count = 0
seen = {}

for key in map.keys():
    if DFS(map, seen, key):
        count += 1

print(count)

#part 2

#print(map)
result = {"ans": 0}
DFS2(map, "shiny gold bag", result, 1)
print(result)
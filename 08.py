#!/bin/python3

def canfinish(lines, visited, idx, acc, result, switch):
    size = len(lines)
    visited = {}

    while idx not in visited:
        visited[idx] = True
        items = lines[idx].split(" ")
        cmd = items[0]
        num = int(items[1])

        if switch:
            if cmd == "nop":
                cmd = "jmp"
            elif cmd == "jmp":
                cmd = "nop"
            switch = False

        if cmd == "nop":
            idx += 1
        elif cmd == "acc":
            acc += num
            idx += 1
        elif cmd == "jmp":
            idx += num

        if idx in visited:
            result["acc"] = acc
            return False

        if idx == size:
            print(idx, "=", size)
            result["acc"] = acc
            return True

    return False

rd = open("08.input", "r")
lines = []

while True:
    line = rd.readline().strip()

    if not line:
        break

    lines.append(line)

acc = 0
idx = 0
visited = {}

while idx not in visited:
    visited[idx] = True
    items = lines[idx].split(" ")
    cmd = items[0]
    num = int(items[1])

    if cmd == "nop":
        idx += 1
    elif cmd == "acc":
        acc += num
        idx += 1
    elif cmd == "jmp":
        idx += num

    if idx in visited:
        break

print(acc)

#part 2

acc = 0
idx = 0
result = {}
visited = {}

while True:
    #print(visited, acc, idx)
    if canfinish(lines, visited.copy(), idx, acc, result, False):
        print(result)
        break
    if canfinish(lines, visited.copy(), idx, acc, result, True):
        print(result)
        break


    visited[idx] = True
    items = lines[idx].split(" ")
    cmd = items[0]
    num = int(items[1])

    if cmd == "nop":
        idx += 1
    elif cmd == "acc":
        acc += num
        idx += 1
    elif cmd == "jmp":
        idx += num


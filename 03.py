#!/bin/python3

rd = open("03.input", "r")
trees = 0
x = 0

right = 1
down = 2

rd.readline()

while True:
    for i in range(down):
        line = rd.readline().strip()

    if not line:
        break

    x = (x + right) % len(line)

    if line[x] == "#":
        trees += 1

print(trees)


# Right 1, Down 1 = 53
# Right 3, Down 1 = 167
# Right 5, Down 1 = 54
# Right 7, Down 1 = 67
# Right 1, Down 2 = 23

# Right 1, Down 1 = 2
# Right 3, Down 1 = 7
# Right 5, Down 1 = 3
# Right 7, Down 1 = 4
# Right 1, Down 2 = 2

#!/usr/bin/python3

filename = "12.input"
rd = open(filename, "r")
direction = 1
wayX = 10
wayY = 1

posX = 0
posY = 0

while True:
    line = rd.readline().strip()

    if line == "":
        break

    command = line[0]
    value = int(line[1:])

    #print(command, value)

    if command == "F":
        posX += (value * wayX)
        posY += (value * wayY)
    elif command == "N":
        wayY += value
    elif command == "S":
        wayY -= value
    elif command == "E":
        wayX += value
    elif command == "W":
        wayX -= value
    elif command == "R":
        rotations = int(value / 90)
        for i in range(0, rotations):
            t = wayX
            wayX = wayY
            wayY = -t

    elif command == "L":
        rotations = int(value / 90)
        for i in range(0, rotations):
            t = wayY
            wayY = wayX
            wayX = -t

    else:
        print("What is this: ", command)

    print(line[0], value, ":", posX, posY, wayX, wayY)

print(posX, posY)

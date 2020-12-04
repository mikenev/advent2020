#!/bin/python3


rd = open("two.input", "r")
total = 0
validTotal = 0

while True:
    line = rd.readline()

    if not line:
        break

    parts = line.split(": ")
    password = parts[1]

    parts = parts[0].split(" ");
    letter = parts[1]
    parts = parts[0].split("-")
    min = int(parts[0])
    max = int(parts[1])
    count = 0

    for l in password:
        if l == letter:
            count += 1
    
    if min <= count and count <= max:
        total += 1

    if password[min-1] != password[max-1]:
        if password[min-1] == letter or password[max-1] == letter:
            validTotal += 1

print(total)
print(validTotal)
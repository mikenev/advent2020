#!/bin/python3

rd = open("06.input", "r")

fullSum =  0
validLetters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" }

while True:
    letters = {}
    count = 0

    while True:
        line = rd.readline().strip()

        if not line or line == "":
            break

        count += 1

        for c in line:
            if c in validLetters:
                if c in letters:
                    letters[c] += 1
                else:
                    letters[c] = 1
    
    if len(letters) == 0:
        break

    for key in letters.keys():
        if letters[key] == count:
            fullSum += 1

print(fullSum)


#!/bin/python3

rd = open("04.input", "r")
numValid = 0
fields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" }

while True:
    needed = fields.copy()
    passport = {}
    lines = []

    while True:
        line = rd.readline().strip()

        if not line or line == "":
            break

        lines.append(line)
    
    if len(lines) == 0:
        break

    for line in lines:
        items = line.split(" ")

        for field in items:
            values = field.split(":")
            valid = True
            key = values[0]

            if key == "byr":
                year = int(values[1])
                valid = 1920 <= year and year <= 2002
            if key == "iyr":
                year = int(values[1])
                valid = 2010 <= year and year <= 2020
            if key == "eyr":
                year = int(values[1])
                valid = 2020 <= year and year <= 2030
            if key == "hgt":
                units = values[1][-2:]
                nums = int(values[1].rstrip("cmin"))
                if units == "cm":
                    valid = 150 <= nums and nums <= 193
                elif units == "in":
                    valid = 59 <= nums and nums <= 76
                else:
                    valid = False
            if key == "hcl":
                valid = values[1][0] == "#" and values[1][1:].rstrip("0123456789abcdef") == "" and len(values[1]) == 7
            if key == "ecl":
                valid = values[1] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth" }
            if key == "pid":
                valid = len(values[1]) == 9 and values[1].rstrip("0123456789") == ""

            if valid:
                passport[key] = values[1]
                needed.remove(key)
            else:
                print("invalid: ", key, ":", values[1])
    
    if len(needed) == 0:
        numValid += 1
    if len(needed) == 1 and "cid" in needed:
        numValid += 1


print(numValid)

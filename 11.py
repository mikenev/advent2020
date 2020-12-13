#!/usr/bin/python3

def iterate(board, rows, cols):
    for r in range(0, rows):
        for c in range(0, cols):
            numAdjacent = numSurrounding(board, rows, cols, r, c)
            if board[r][c] == "L" and numAdjacent == 0:
                board[r][c] = "l"
            elif board[r][c] == "#" and numAdjacent >= 4:
                board[r][c] = "3"

    result = ""

    for r in range(0, rows):
        for c in range(0, cols):
            if board[r][c] == "l":
                board[r][c] = "#" # occupied
            if board[r][c] == "3":
                board[r][c] = "L"
            result += board[r][c]
        result += "\n"

    return result


def numSurrounding(board, rows, cols, r, c):
    num = 0
    cols -= 1
    rows -= 1

    if r > 0 and c > 0 and (board[r-1][c-1] == "#" or board[r-1][c-1] == "3"):
        num += 1
    if r > 0 and (board[r-1][c] == "#" or board[r-1][c] == "3"):
        num += 1
    if r > 0 and c < cols and (board[r-1][c+1] == "#" or board[r-1][c+1] == "3"):
        num += 1
    
    if c > 0 and (board[r][c-1] == "#" or board[r][c-1] == "3"):
        num += 1
    if c < cols and (board[r][c+1] == "#" or board[r][c+1] == "3"):
        num += 1

    if r < rows and c > 0 and (board[r+1][c-1] == "#" or board[r+1][c-1] == "3"):
        num += 1
    if r < rows and (board[r+1][c] == "#" or board[r+1][c] == "3"):
        num += 1
    if r < rows and c < cols and (board[r+1][c+1] == "#" or board[r+1][c+1] == "3"):
        num += 1

    #print(r, c, num)

    return num

filename = "11.input"
rd = open(filename, "r")
lines = []

while True:
    line = rd.readline().strip()

    if not line:
        break

    lines.append(list(line))

rows = len(lines)
cols = len(lines[0])

prev = ""

while True:
    current = iterate(lines, rows, cols)
    #print(current)

    if current == prev:
        break

    prev = current

cnt = 0

for r in range(0, rows):
    for c in range(0, cols):
        if lines[r][c] == "#":
            cnt += 1

print(cnt)
#!/usr/bin/python3

def iterate(board, rows, cols):
    for r in range(0, rows):
        for c in range(0, cols):
            if board[r][c] == ".":
                continue
            numAdjacent = numSurrounding(board, rows, cols, r, c)
            if board[r][c] == "L" and numAdjacent == 0:
                board[r][c] = "l"
            elif board[r][c] == "#" and numAdjacent >= 5:
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

    if occupiedInDirection(board, rows, cols, r-1, c-1, -1, -1):
        num += 1
    if occupiedInDirection(board, rows, cols, r-1, c, -1, 0):
        num += 1
    if occupiedInDirection(board, rows, cols, r-1, c+1, -1, 1):
        num += 1

    if occupiedInDirection(board, rows, cols, r, c-1, 0, -1):
        num += 1
    if occupiedInDirection(board, rows, cols, r, c+1, 0, 1):
        num += 1

    if occupiedInDirection(board, rows, cols, r+1, c-1, 1, -1):
        num += 1
    if occupiedInDirection(board, rows, cols, r+1, c, 1, 0):
        num += 1
    if occupiedInDirection(board, rows, cols, r+1, c+1, 1, 1):
        num += 1

    #print(r, c, num)

    return num

def occupiedInDirection(board, rows, cols, r, c, incR, incC):
    while r >= 0 and c >= 0 and r < rows and c < cols:
        if board[r][c] == "#" or board[r][c] == "3":
            return True
        if board[r][c] == "L" or board[r][c] == "l":
            return False
        r += incR
        c += incC

    return False

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
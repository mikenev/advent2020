#!/usr/bin/python3

filename = "10.input"
rd = open(filename, "r")
lines = []
mx = 0

while True:
    line = rd.readline().strip()

    if not line:
        break

    val = int(line)
    mx = max(mx, val)

    lines.append(int(line))

lines.append(mx+3)
lines.sort()

prev = 0
diff1 = 0
diff3 = 0

for i in lines:
    if i - prev == 1:
        diff1 += 1
    elif i - prev == 3:
        diff3 += 1
    else:
        print(i, "-", prev, "=", i-prev)

    prev = i

print(diff1, diff3)
print(diff1 * diff3)

def DFS(nums, idx, result):

    #print(idx)
    if nums[idx] == nums[-1]:
        result["count"] += 1
        return

    i = idx + 1
    end = len(nums)

    while i < end and nums[i] <= nums[idx] + 3:
        DFS(nums, i, result)
        i += 1

    return


# part 2

d = {0: 1}
i = 0

for i in lines:
    c = 0
    for j in [i-1, i-2, i-3]:
        if j in d:
            c += d[j]
    d[i] = c
#print(d)

print(d[mx])



#!/bin/python3

from queue import Queue

rd = open("09.input", "r")
preamble = 25
nums = []
avail = {}

for i in range(0, preamble):
    line = int(rd.readline().strip())
    nums.append(line)
    avail[line] = True

insIdx = 0
target = 0

while True:
    line = rd.readline().strip()

    if not line:
        break

    num = int(line)
    found = False

    for i in nums:
        needed = num - i
        #print(num, ", i=", i, " needed=", needed)
        if needed < 0 or needed == i:
            continue

        if needed in avail:
            old = nums[insIdx]
            nums[insIdx] = num
            avail.pop(old)
            avail[num] = True
            insIdx += 1
            insIdx = insIdx % preamble
            found = True
            #print("nums", nums)
            #print("avail", avail)
            break

    if not found:
        target = num
        
        break

print (target, "is invalid")
rd.close()

# part 2
rd = open("09.input", "r")
q = Queue()
sum = 0

while True:
    line = rd.readline().strip()
    
    if not line:
        break;

    num = int(line)
    q.put(num)
    sum += num

    if sum < target:
        continue

    while sum > target:
        sum -= q.get()

    if sum == target:
        print("found")
        min = q.get()
        max = min

        while not q.empty():
            item = q.get()
            if item < min:
                min = item
            if item > max:
                max = item

        print(min + max)
        break


import bisect

tuples = int(input())

aList = []
bList = []
cList = []
dList = []

for row in range(tuples):
    a, b, c, d = map(int, input().split())

    aList.append(a)
    bList.append(b)
    cList.append(c)
    dList.append(d)


ab = [x+y for x in aList for y in bList]
cd = [x+y for x in cList for y in dList]


ab.sort()
cd.sort()

count = 0
index = 0
while index < len(ab):

    x = ab[index]

    repetitions = 0
    while index < len(ab) and x == ab[index]:
        index += 1
        repetitions += 1

    lower = bisect.bisect_left(cd, -x)
    upper = bisect.bisect_right(cd,-x, lower)

    if lower != upper:
        count = count + (upper - lower)*repetitions

print(count)


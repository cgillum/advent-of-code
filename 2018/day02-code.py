import os
import sys

def part1(ids):
    twoCharLabels = 0
    threeCharLabels = 0
    for id in ids:
        counts = {}
        for c in id:
            count = counts.setdefault(c, 0)
            counts[c] = count + 1
        
        found2 = False
        found3 = False
        for c, count in counts.items():
            if not found2 and count == 2:
                twoCharLabels += 1
                found2 = True
            elif not found3 and count == 3:
                threeCharLabels += 1 
                found3 = True

    checksum = twoCharLabels * threeCharLabels
    print(f'Part 1 - Checksum: {checksum}')


def part2(ids):
    for i in range(len(ids)):
        id1 = ids[i]
        for j in range(i + 1, len(ids)):
            id2 = ids[j]
            different = 0
            common = []
            for c in range(len(id1)):
                if (id1[c] == id2[c]):
                    common.append(id1[c])
                else:
                    different += 1
                    if different > 1:
                        break
            
            if different == 1:
                print(f'Found off-by-ones: {id1.strip()} and {id2.strip()}')
                print(f'Part 2 - Common: {"".join(common).strip()}')
                return


with open(os.path.join(sys.path[0], 'day02-input.txt')) as inputFile:
    ids = inputFile.readlines()
    part1(ids)
    part2(ids)
    
import os
import re
import sys

class Rect:

    # example input: #15 @ 192,982: 10x13
    pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, id, left, top, width, height):
        self.id = id
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __str__(self):
        return f'#{self.id} @ {self.left},{self.top}: {self.width}x{self.height}'

    def intersect(self, r):
        left = max(self.left, r.left)
        right = min(self.left + self.width, r.left + r.width)
        width = right - left
        if (width < 0): return None
        
        top = max(self.top, r.top)
        bottom = min(self.top + self.height, r.top + r.height)
        height = bottom - top
        if (height < 0): return None
        
        return Rect(0, left, top, width, height)

    def flatten(self, rowSize):
        indexes = []
        for y in range(self.height):
            for x in range(self.width):
                index = (self.left + x) + (self.top + y)*rowSize
                indexes.append(index)
        return indexes
    
    @classmethod
    def fromText(cls, text):
        match = cls.pattern.match(line)
        (id, left, top, width, height) = match.groups()
        return cls(int(id), int(left), int(top), int(width), int(height))


with open(os.path.join(sys.path[0], 'day03-input.txt')) as inputFile:
    claims = []
    for line in inputFile:
        r = Rect.fromText(line)
        claims.append(r)

overlappedSquares = {}
claimConflicts = {}
for i in range(len(claims)):
    for j in range(i + 1, len(claims)):
        c1 = claims[i]
        c2 = claims[j]
        intersection = c1.intersect(c2)
        if intersection is not None:
            claimConflicts.setdefault(c1, 0)
            claimConflicts[c1] += 1
            claimConflicts.setdefault(c2, 0)
            claimConflicts[c2] += 1
            for index in intersection.flatten(1000):
                overlappedSquares.setdefault(index, 1)
                overlappedSquares[index] += 1

print(f'Part 1 - Overlapped count: {len(overlappedSquares)}')

isolatedClaims = [c.id for c in claims if c not in claimConflicts]
print(f'Part 2 - Isolated claim IDs: {isolatedClaims}')
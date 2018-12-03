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
    
    r = claims[0].intersect(claims[1])
    print(r)



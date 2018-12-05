import collections
import os
import sys

# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up

class Guard:
    def __init__(self, id):
        self.id = id
        self.awake = True
        self.sleeps = collections.defaultdict(int)
        self.total_sleep = 0
        self.favorite = -1
        self.favorite_recurrences = 0

    def sleeping(self, minute):
        self.sleep_start = minute
        self.awake = False

    def awoke(self, minute):
        for m in range(self.sleep_start, minute):
            self.total_sleep += 1
            recurrences = self.sleeps.get(m, 0) + 1
            self.sleeps[m] = recurrences
            if recurrences > self.favorite_recurrences:
                self.favorite = m
                self.favorite_recurrences = recurrences
        self.awake = True

guards = {}
with open(os.path.join(sys.path[0], 'day04-input.txt')) as file:
    sorted_lines = sorted(file.readlines())
    current = None
    for line in sorted_lines:
        date = line[1:17]
        action = line[19:-1]
        minute = int(date[-2:])
        if action.startswith("Guard"):
            if current is not None and not current.awake:
                current.awoke(minute)
            next_id = int(action[7:-13])
            if next_id in guards:
                current = guards.get(next_id)
            else:
                current = Guard(next_id)
                guards[next_id] = current
        if action == "falls asleep":
            current.sleeping(minute)
        elif action == "wakes up":
            current.awoke(minute)

# Part 1: Find the guard that has the most minutes asleep.
#         What minute does that guard spend asleep the most?
#         What is the ID of the guard you chose multiplied by the minute you chose?
biggest_sleeper = max(guards.items(), key=lambda g: g[1].total_sleep)[1]
favorite_minute = biggest_sleeper.favorite
result = biggest_sleeper.id * favorite_minute
print(f'Part 1 - Result: {result}')

# Part 2: Of all guards, which guard is most frequently asleep on the same minute?
#         What is the ID of the guard you chose multiplied by the minute you chose?
most_consistent_sleeper = max(guards.items(), key=lambda g: g[1].favorite_recurrences)[1]
favorite_minute = most_consistent_sleeper.favorite
result = most_consistent_sleeper.id * favorite_minute
print(f'Part 2 - Result: {result}')

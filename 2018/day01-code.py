import os, sys

sum = 0
runningTotal = 0
repeatedFrequency = 0
knownFrequencies = set()

with open(os.path.join(sys.path[0], 'day01-input.txt')) as inputFile:
    # Buffer into memory since we'll read through it multiple times
    allLines = inputFile.readlines()

    # Part 1: compute the sum of all lines
    for line in allLines:
        sum += int(line)

    # Part 2: find the first repeating frequency
    iterations = 0
    done = False

    while True:
        if (iterations >= 1000000):
            print('ERROR: Infinite loop detected!')
            break

        for line in allLines:
            runningTotal += int(line)
            if runningTotal in knownFrequencies:
                repeatedFrequency = runningTotal
                done = True
                break
            knownFrequencies.add(runningTotal)
        
        if done:
            break

        iterations += 1

print(f'Part 1: {sum}')
print(f'Part 2: {repeatedFrequency}')

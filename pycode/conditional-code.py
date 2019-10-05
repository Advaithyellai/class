import random

nonUniqueList = []

for loop in range(0, 150):
    nonUniqueList.append(random.randrange(0, 100))

uniqueList = []

print(len(nonUniqueList))

for nonUnqiueItem in nonUniqueList:
    if nonUnqiueItem not in uniqueList:
        uniqueList.append(nonUnqiueItem)

print(len(uniqueList))
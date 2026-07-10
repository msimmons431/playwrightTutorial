sortme=[33,3,5,9,12,1,2,22]
n = len(sortme)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1 ):
        if sortme[j] > sortme[j + 1]:
            sortme[j], sortme[j + 1] = sortme[j + 1], sortme[j]
            swapped = True
    if not swapped:
        break

print(sortme)
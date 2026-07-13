sortme=[33,3,5,9,12,1,2,22]
n = len(sortme)
for i in range(n):
    print(f"Step 1: i (outer loop) ( range 0 - len(array) ) is {i}")
    print(f"Step 2: swapped = False ( this is the default.")
    swapped = False
    for j in range(0, n - i - 1 ):
        print(f"INFO: The value of i ( outer loop) is ({i}) and j ( inner loop ) is {j}")
        print(f"Step 3: j {j} is equal to the len of the array minus i ( current value for inner loop ) {i}")
        print(f"Step 4: IF sortme[{j}] {sortme[j]} GREATE THAN sortme[{j+1}] {sortme[j+1]} THEN LETS SWAP.")
        if sortme[j] > sortme[j + 1]:
            sortme[j], sortme[j + 1] = sortme[j + 1], sortme[j]
            swapped = True
    if not swapped:
        break

print(sortme)
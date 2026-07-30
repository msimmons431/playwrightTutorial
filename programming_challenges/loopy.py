n = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
foo = len(n)

for outer in range(
    0, len(n)
):  # This just controls how many times to loop through the array
    for inner in range(
        0, foo - outer - 1
    ):  # This is what evaluates the values in the array.
        print(f"OUTER is {outer} AND INNER is {inner}")
        print(f"Current value is {n[inner]}")

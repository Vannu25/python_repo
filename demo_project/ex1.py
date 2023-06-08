picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# 1.iterate over picture.
# 2. print empty space - ' ' if it hits 0.
# 3. print '*' if it hits 1.


for i in picture:
    for j in i:
        if j == 0:
            print(" ", end='')

        elif j == 1:
            print("*", end='')
    print('')  # need a new line after every row(i)

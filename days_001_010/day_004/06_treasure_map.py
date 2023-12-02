# Treasure Map

#    A  B   C
# 1 [ ][ ][ ]
# 2 [ ][ ][ ]
# 3 [ ][ ][ ]

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

cols = ["A", "B", "C"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure (e.g. B2)? ")

col = position[0]
row = position[1]

col_num = cols.index(col.upper())
row_num = int(row) - 1

map[row_num][col_num] = "X"

print(f"{line1}\n{line2}\n{line3}")
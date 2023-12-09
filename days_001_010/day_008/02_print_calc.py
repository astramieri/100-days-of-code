import math

def print_calc(height, width):
    coverage = 5 # square meters
    num_cans = math.ceil((height * width) / coverage)
    print(f"Number of cans: {num_cans}")

h = int(input("Height of the wall (m): "))
w = int(input("Width of the wall (m): "))

print_calc(h, w)

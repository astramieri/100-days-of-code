## Average Heights

heights = "78 65 89 86 55 91 64 89"

heights_list = heights.split(" ")

max_height = 0
total_height = 0

for i in range(0, len(heights_list)):
    total_height += int(heights_list[i])

    if int(heights_list[i]) > max_height:
        max_height = int(heights_list[i])

average_height = int(total_height / len(heights_list))

print(f"Total height = {total_height}")
print(f"Number of students = {len(heights_list)}")
print(f"Average height = {average_height}")
print(f"Max height = {max_height}")
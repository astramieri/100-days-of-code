for number in range(1, 10): # not including 10!
    print(number)

for number in range(1, 10, 3):
    print(number)

total_sum = 0

for number in range(1, 101):
    total_sum += number

print(f"The total sum is {total_sum}.")
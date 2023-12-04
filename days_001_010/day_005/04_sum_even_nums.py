target = int(input("Enter a number btween 1 and 100. "))

sum_of_even = 0
even_nums = []

for i in range(0, target + 1, 2):
    sum_of_even += i
    even_nums.append(i)

print(f"The sum of even numbers between 1 and {target} is {sum_of_even}.")
print(even_nums)

sum_of_even = 0
even_nums = []

for i in range(1, target + 1):
    if i % 2 == 0:
        sum_of_even += i
        even_nums.append(i)

print(f"The sum of even numbers between 1 and {target} is {sum_of_even}.")
print(even_nums)


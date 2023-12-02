my_list =["apple", True, 2, 5.6] #  alist is an ordered data structure of any datatype

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print(my_list[-1]) # last
print(my_list[-2]) # second last

my_list[1] = False

print(my_list[1])

my_list.append("Arizona")

print(my_list[-1])

my_list.extend(["Arizona", 45.67])

print(my_list)
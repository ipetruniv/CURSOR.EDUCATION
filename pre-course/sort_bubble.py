my_list = [1, 3, 5, 4, 3, 11, 50, 40, 30]
print(my_list)
print(len(my_list))
sorted = 0

for i in range(len(my_list)):
	if my_list[i] > my_list[i + 1]:
		tmp = my_list[i]
		my_list[i] = my_list[i + 1]
		my_list[i + 1] = tmp

print(my_list)



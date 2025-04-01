#empty list
my_list =[]

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value 15 at second position in list
my_list.insert(1,15)

# extend my_list with another list
my_list.extend([50,60,70])

#remove last element from my_list
my_list.pop()

#sort my_list in ascending order
my_list.sort()

#find and print the index of value 30 in my_list
index_of_30 = my_list.index(30)

print(f"The index of 30 is: {index_of_30}")




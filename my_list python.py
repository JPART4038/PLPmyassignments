my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert the value 15 at the second position in the list
my_list.insert(1,15)
#extend my list
my_list.extend([50,60,70])

#Remove the last element from my list

my_list.pop()

#sort my list in ascnding order
my_list.sort

#find and print the index of the value 30 
index_of_30 = my_list.index(30)
print('my_list',my_list)
print('index of value 30: ',index_of_30)
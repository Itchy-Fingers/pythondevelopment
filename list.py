my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position
my_list.insert(1, 15)

  # Extending the list with three more elements  
my_list.extend([50, 60, 70])  

# Removing the first element
my_list.pop()    

# Sorting the list in ascending order 
my_list.sort()   

# Finding and printing the index of the value 30
print(my_list.index(30))
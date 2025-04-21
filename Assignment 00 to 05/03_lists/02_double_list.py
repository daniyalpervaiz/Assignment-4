# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

list_items=[2,4,6,8]
for items in range(len(list_items)):
    index_items=list_items[items]
    list_items[items]=index_items*2
   
print(list_items)


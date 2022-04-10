"""
1.Using append() method

"""
#1
# Addition of elements in a List
list=[]
print("Initial blank list :")
print(list)

# Addition of Elements 
# in the List
list.append(1)
list.append(3)
list.append(6)
print("after adding elements in a list :")
print(list)

# Adding elements to the List
# using Iterator

for i in range(1,4):
    list.append(i)
print("after adding elements from 1-3:")
print(list)


# Adding Tuples to the List


list.append((4,3))

print("after adding tuple:")
print(list)

# Addition of List to a List

list2=['red','yellow']
list.append(list2)
print("after adding list into the list:")
print(list)

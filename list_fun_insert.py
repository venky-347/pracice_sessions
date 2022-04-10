# Addition of elements in a List
   
# Creating a List

list=[12,34,45,67]
print("Initial list :")
print(list)

list.insert(3,5)
list.insert(0,"venky")
print("after inserting into the lst :")

print(list)

print("length of the list :",len(list))

#Using extend() method

list_e=[2,5,7,9]
print("initial list :")
print(list_e)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)

list_e.extend([99,"venky",99.99])
print("\n after perfroming extend function:")
print(list_e)

#Accessing elements from the List

# Creating a List with
# the use of multiple values

list_a=["venky","john","venkat"]
print("accesing elements from the list :")
print(list_a[0])
print(list_a[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)

list_n=[['ram','lakshman'],['seetha']]

# accessing an element from the 
# Multi-Dimensional List using
# index number

print("accesing an element from the multi dimensional list :")
print(list_n[0][1])
print(list_n[1][0])


#Negative indexing

list_neg=[1,2,4,"venky",45,67,780,123]
# accessing an element using
# negative indexing
print("accesing elements using negative indexing")
print("last element of the list :")
print(list_neg[-1])

print("thid last element from the last ")
print(list_neg[-3])


#Using remove() method

# Removal of elements in a List

list_r=[1,2,3,4,5,6,456,345,143,145]

print("initial list :")
print(list_r)

list_r.remove(456)
list_r.remove(345)
print("after removing 2 elements :")
print(list_r)

# Removing elements from List
# using iterator method

for i in range(1,5) :
    list_r.remove(i)
print("\n after remvoing a range of elements :")
print(list_r)

#Using pop() method

list_p=[1,2,3,4,5,6,7,8]
# Removing element from the 
# Set using the pop() method
list_p.pop()
print("after popping an element:")
print(list_p)


# Removing element at a 
# specific location from the 
# Set using the pop() method

list_p.pop(3)
print("after popping a specific element :")
print(list_p)

#Slicing of a List
# Removal of elements in a List

#creating list
list_slice=['v','e','n','k','y','s','o','l','o']
print("initial list :")
print(list_slice)
sliced_list=list_slice[3:8]
print("\n Slicing elements in a range 3-8:")
print(sliced_list)

# Print elements from a 
# pre-defined point to end

sliced_list_a=list_slice[5:]
print("\n elements sliced from 5th element to till end :")
print(sliced_list_a)

# Printing elements from
# beginning till end

sliced_list_b=list_slice[:]
print("\n printing all elements using slice operarion:")
print(sliced_list_b)

#Negative index List slicing

#create a list
list_index=['h','e','l','l','o','w','e','l','c','o','m','e']
print("print initial list before index slicing :")
print(list_index)

# Print elements from beginning
# to a pre-defined point using Slice

sliced_list_index_1=list_index[:-6]
print("\n elements sliced till 6th element from last :")
print(sliced_list_index_1)

# Print elements of a range
# using negative index List slicing
neg_sliced_index=list_index[-6:-1]
print("\n elements sliced from index -6 to -1:")
print(neg_sliced_index)

#printing elements in reverse 
#using slice operation

revr_slice=list_index[::-1]

print("\n printing list in reverse :")
print(revr_slice)

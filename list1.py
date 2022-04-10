"""
1.creating a list
2.creating a list of numbers
3.# Creating a List of strings and accessing
    # using index
4.# Creating a Multi-Dimensional List
    # (By Nesting a list inside a List)
5.Creating a list with multiple distinct or duplicate elements

"""

#1.create list

List=[]
print("blank list :")
print(List)


#2

list_numbers=[4,5,6]
print("\n list of numbers :")
print(list_numbers)

#3

list_index=["venky","john","venkat"]
print("\n list of items(index) :")
print(list_index[0])
print(list_index[2])

#4

multi_list=[['apple','banana'],['orange']]

print("\n multi dimension list :")
print(multi_list)

print(multi_list[0])

#5

# Creating a List with 
# the use of Numbers
# (Having duplicate values)

list=[1,2,3,2,2,5,5,6,7,88,99,4,0]

print("list of numbers :")
print(list)

# Creating a List with 
# mixed type of values
# (Having numbers and strings)


list_mul=[1,2,0.2,"venky",6,7,True]

print("list of multi values :")
print(list_mul)
print(type(list_mul[6]))

#Knowing the size of List

list_size=[]
print("size of the list :")
print(len(list_size))

list_size1=[2,4,6,8,9]
print("size of the list :")
print(len(list_size1))

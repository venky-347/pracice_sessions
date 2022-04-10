"""
List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.

A list comprehension consists of brackets containing the expression, which is executed for each element along with 
the for loop to iterate over each element.

Syntax:

newList = [ expression(element) for element in oldList if condition ]

"""
# Python program to demonstrate list 
# comprehension in Python 

# below list contains square of all 
# odd numbers from range 1 to 10 

odd_square=[x**2 for x in range(1,11) if x%2==1]
"""
x**2-->output expression
range(1,11)-->input sequence
x is variable and 
if x%2==1 is predicate part(condition)
"""
print("printing elements using list compression :",odd_square)

# for understanding, above generation is same as, 
odd_square_1=[]

for x in range(1,11):
    if x%2==1:
        odd_square_1.append(x**2)
print("printing elements in normal way:",odd_square_1)


# below list contains power of 2 from 1 to 8 

power_of_2=[2**x for x in range(1,11)]
print("\n powers of 2 values:")
print(power_of_2)

# below list contains prime and non-prime in range 1 to 50 

noprimes=[j for i in range(2,8) for j in range(i*2,50,i)]
primes=[x for x in range(2,50) if x not in noprimes]
print(primes)

# list for lowering the characters 
print("printing values from upper to lower case:")

print([x.lower() for x in ["v","E","N","K","Y"]])

#list for uppercase from the charecters

print("printing values from lower to upper case:")
print([x.upper() for x in ["s","o","l","o"]])

#list which extract number

string="my mobile number is : 12345 $!67890"
print("\n extraced digits :")
numbers=[x for x in string if x.isdigit()]
print(numbers)

# A list of list for multiplication table 
a=7
table=[[a,b,a * b] for b in range(1,11)]
print("\n multiplication table is :")
for i in table :
    print(i)
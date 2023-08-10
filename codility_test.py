import random
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# N = input(print('Please give me the number of elemnets in the list: '))
# A = [1, 3, 6, 4, 1, 2] (5)
# A = [1, 2, 3] (4)
# A = [-1, -3]
# A = [1, 3, 6, 4, 1, 2, -5, -11, -3]
B_only_positive_integers_list = []
C_unique_element_list = []
A = []
N = random.randint(1,10)
print('The number of elemnets in the list:', N)

def create_random_list():
    for x in range(N):
        number = random.randint(0, 10)
        A.append(number)

create_random_list()
print('The list:', A ) 


# remove all the negative numbers and 0 -------------------------------
for x in A:
    if x >= 0:
        B_only_positive_integers_list.append(x)

print('The positive numbers list:', B_only_positive_integers_list ) 


# create an unique list ------------------------------------------------
for x in B_only_positive_integers_list:
    if x not in C_unique_element_list:
        C_unique_element_list.append(x)

print('The unique_elements:', C_unique_element_list )


# create a sorted list -------------------------------------------------
C_unique_element_list.sort()

print('The sorted list:', C_unique_element_list ) 


# find the smallest positive integer -----------------------------------
smallest_positive_integer = 1
for x in C_unique_element_list:
    if x == smallest_positive_integer:
        smallest_positive_integer += 1
print('Smallest positive integer (greater than 0) that does not occur in A:', smallest_positive_integer)
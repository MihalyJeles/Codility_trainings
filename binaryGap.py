# def binarygap(number):
#     format(number, 'b')
#     return

#  0.) Ask for the integer ------------------------------------------------
number = int(input('Please give me an integer number: '))
#  1.) turn the integer into binary format --------------------------------
binary_number = bin(number)[2:]
print(binary_number)
#  2.) interate and find the binarygaps and lenght of it-------------------
binary_length_list = []
binary_gaps = 0
for i in binary_number:
    if  i == 1:
        bin = 1
        if binary_length > 0:
            binary_length_list.append(binary_length)
            binary_length = 0
    if i == 0:
        if bin == 1:
            binary_gaps += 1
            bin = 0
        binary_length =+ 1
print(binary_length_list)
max_length = max(binary_length_list)
print(f'The number {number}, has binary representation {binary_number} and contains {binary_gaps} binary gaps. Max length of it {max_length}')

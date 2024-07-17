immutable_var = 1, 2, 'three', 'four'
print(immutable_var)
#immutable_var[0] = 10
#Tuples aren't changeable so as to retain the integrity of the list or information, which we don't want changed.
#Also, tuples take up less memory space than lists.

mutable_list = ([1, 2], 'three', 'four')
print(mutable_list)
mutable_list[0][1] = 3
print(mutable_list)

'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]
new_list=[]
other_list=[]

for numbers in list_two:
    if numbers in list_one:
        new_list.append(numbers)
        list_one.remove(numbers)
        list_two.remove(numbers)
    else:
        other_list.append(numbers)

another_list = list_one+list_two



print(new_list,another_list)

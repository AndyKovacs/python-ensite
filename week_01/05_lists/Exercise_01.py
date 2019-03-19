'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''
#numbers = int(input('numbers: '))
numbers_list = [1,2,3,4,5,6,7,8,9,10]

#numbers = list(numbers)
for numbers in numbers_list:
    sum = numbers_list[numbers]+numbers_list[numbers+1]

print(sum)
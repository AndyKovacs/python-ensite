'''
There are many string methods available to perform all sorts of tasks.

Experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

Python documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

For this exercise, demonstrate the following string methods below:
- strip
- replace
- find

'''
# some exmaples
my_name =' Andy '
my_surname =' kovacs '
my_middlename = ' jenö '

print(my_name.lstrip())

print(my_surname.rstrip())

print(my_middlename.strip())

print(my_name.replace('A','B'))
print(my_name.find('d')) # Andy is the word what is tested...it should give a 3
print(my_middlename.find('n'))
print(my_surname.find('c'))
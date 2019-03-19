'''
Write a script that finds the first vowel in a a user inputted string.

'''
name = input("give a word: ")
vowels =['a','e','i','o','u']
#print(name.find('a'))
#print(name.find('e'))
#print(name.find('i'))
#print(name.find('o'))
#print(name.find('u'))

#print(name)

for letter in name:
    if letter in vowels:
        print(letter)
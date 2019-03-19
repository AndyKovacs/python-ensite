'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
user_input =input('gimme your stuff: ')
print(user_input.upper())
print(user_input.lower())
vowels = ['a','e','i','o','u']

for letter in user_input:
    if letter in vowels:
        print(letter.lower())
    else:
        print(letter.upper())

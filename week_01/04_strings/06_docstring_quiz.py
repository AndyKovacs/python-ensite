'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''

def any_lowercase1(s):  # i guess this works
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):# this is not working, cause c is not defined, and true and false are stringe and not boolean
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): # dont know what the heck it is flag should be at least assigned to True or False
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):      # i dont know, i guess this is bullshit
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower(): # would work if the else statement after return fals is set....
            return False
    return True

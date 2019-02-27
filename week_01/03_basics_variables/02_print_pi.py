'''
Print pi to the console using the following formula:
note that this is not the complete series to compute the true number pi.
Challenge: find another way to do this using a package you can import

4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

'''
a = 4.0
b = (1-1.0/3)
c = (1.0/5)
d = (1.0/7)
e = (1.0/9)
f = (1.0/11)
g = a*(b+c-d+e-f)
print(g)
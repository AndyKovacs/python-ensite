'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''

celsius = float(input("give your temperature in: "))
f = celsius*1.8+32
#celsius = (f-32)/1.8
#one_degree = (1*f-32)/1.8

print(f"{celsius}°C={f}Fahrenheit")

'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
population = 380123456
period_of_time_in_sec =(3*60*60*24*365)
born_in_3years = period_of_time_in_sec/6
dies_in_3years = period_of_time_in_sec/12
immigrates_in_3years = period_of_time_in_sec/40
pop_in_3years= population+born_in_3years-dies_in_3years+immigrates_in_3years
print(pop_in_3years)
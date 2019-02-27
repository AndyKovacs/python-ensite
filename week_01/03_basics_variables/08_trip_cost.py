'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
miles_to_drive = float(input("how many miles you're planning to drive?: "))
MPG_of_the_car = float(input("how many miles per Gallon can your car drive?: "))
price_per_gallon = float(input("price per gallon of fuel: "))
cost = miles_to_drive/MPG_of_the_car*price_per_gallon
print(f"the cost of your trip will be {cost} dollars.")


"""
Ask a user their weight (in pounds),
convert it to kilograms and print on the screen.
"""

#SOLUTION
weight_lbs = input('Enter your weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print('Your weight from lbs to kg is: ' + str(weight_kg))
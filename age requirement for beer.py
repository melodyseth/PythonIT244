age = int(input('Please state your age: '))
    
if age < 21:
    noAlcoholOrder = str(input('Which non-alcoholic beverage would you like?'))
    okToOrderDrink = 'Sorry, you are too young! Here is your ' + noAlcoholOrder + "."
else:
    drinkOrder = str(input('What kind of drink would you like? '))
    okToOrderDrink = "Here is your " + drinkOrder + "."
print("You are {}.".format(age) , okToOrderDrink)

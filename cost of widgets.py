COST_PER_WIDGET = 7.49
#Constant price of one widget
nWidgets = input ('How many widgets do you want to buy? ')
nWidgets = int(nWidgets)
#Convert to an integer
if nWidgets == 1:
    print('One widget will cost you $' , COST_PER_WIDGET)
else:
    cost = nWidgets * COST_PER_WIDGET
    print(nWidgets, 'widgets will cost you $', cost)

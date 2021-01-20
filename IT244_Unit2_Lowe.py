#Displays list of colors for user to input.
print("Your color choices are red, blue, green, white, or yellow.")
#Ask user to input color from list.
userColor =str(input("Enter a color from the list above: "))
validColor = True
#Changes all letter cases from user input to lowercase.
userColor = userColor.lower()
#Defines user color and translates it to Spanish.
if userColor == "red":
    spanishColor = "rojo"
elif userColor == "blue":
    spanishColor = "azul"
elif userColor == "green":
    spanishColor = "verde"
elif userColor =="white":
    spanishColor = "blanco"
elif userColor == "yellow":
    spanishColor = "amarillo"
#Creates a case for if the users input is not in the list.
else:
    validColor = False
#Prints a sentence with the users inputs if the input is valid.
if validColor:
    print("The color",userColor,"in Spanish is {}.".format(spanishColor))
#Prints a sentence if the users input is not valid.
else:
    print("That is not a valid color for this program. Ese no es un color válido.")

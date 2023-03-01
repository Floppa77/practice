# imports
import Data
import gooeypie as gp

# Define occupant objects with values
occupant1 = Data.useValues(1, 13.1, 10.6)
occupant2 = Data.useValues(2, 16.3, 13.9)
occupant3 = Data.useValues(3, 18.3, 15.8)
occupant4 = Data.useValues(4, 21, 18.6)
occupant5 = Data.useValues(5, 23.1, 20.6)
occupant6 = Data.useValues(6, 25.3, 22.8)

def getOccupants(amount):
    global activeObject
    if amount == 1:
        activeObject = occupant1
    elif amount == 2:
        activeObject = occupant2
    elif amount == 3:
        activeObject = occupant3
    elif amount == 4:
        activeObject = occupant4
    elif amount == 5:
        activeObject = occupant5
    elif amount == 6:
        activeObject = occupant6

def checkEnergy():
    if option == 1:
        userUse = input("How much energy do you use: ")
        if float(userUse) < activeObject.electricUse:
            print("Congrats")
        elif float(userUse) < activeObject.electricUse + 1:
            print("Increase Home Insulation")
        elif float(userUse) > activeObject.electricUse:
            print("increase your home insulation and switch off your second fridge.")
    elif option == 2:
        userUse = input("How much energy do you use: ")
        if float(userUse) < activeObject.gasUse:
            print("Congrats")
        elif float(userUse) < activeObject.gasUse + 1:
            print("Increase Home Insulation")
        elif float(userUse) > activeObject.gasUse:
            print("increase your home insulation and switch off your second fridge.")

active = getOccupants(int(input("Amount of people in house: ")))
option = int(input("Select:\n[1] Electric Hot Water\n[2] Gas Hot Water\n"))
checkEnergy()


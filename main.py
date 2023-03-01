#imports
import data 
import gooeypie as gp



# Define occupants objects with values
occupant1 = data.useValues(1, 13.1, 10.6)
occupant2 = data.useValues(2, 16.3, 13.9)
occupant3 = data.useValues(3, 18.3, 15.8)
occupant4 = data.useValues(4, 21, 18.6)
occupant5 = data.useValues(5, 23.1, 20.6)
occupant6 = data.useValues(6, 25.3, 22.8)

# Request number of occupants and Electric or Gas
intNumPeople = int(input("Enter number of occupants: "))
option = int(input("Select:\n[1] Electric Hot Water\nOr\n[2] Gas Hot Water\n"))



if intNumPeople == 1:
    activeObject = occupant1
elif intNumPeople == 2:
    activeObject =occupant2
elif intNumPeople == 3:
    activeObject =occupant3
elif intNumPeople == 4:
    activeObject =occupant4
elif intNumPeople == 5:
    activeObject =occupant5
elif intNumPeople == 6:
    activeObject =occupant6


# 
if option == 1:
    userUse = input("How much energy do you use: ")
    if float(userUse) < activeObject.electricUse:
        print("Congrats! You're under")
    elif float(userUse) < activeObject.electricUse + 1:
        print("Increase Home Insulation")
    elif float(userUse) > activeObject.electricUse:
        print("increase your home insulation and switch off your second fridge.")
elif option == 2:
    userUse = input("How much energy do you use: ")
    if float(userUse) < activeObject.gasUse:
        print("Congrats! You're under")
    elif float(userUse) < activeObject.gasUse + 1:
        print("Increase Home Insulation")
    elif float(userUse) > activeObject.gasUse:
        print("increase your home insulation and switch off your second fridge.")

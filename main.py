#Import libaries
import time
import sys
import os

#Default generation values
popNumJuv = 10
popNumAdults = 10
popNumSen = 10

survNumJuv = 1
survNumAdults = 1
survNumSen = 0

birthRate = 2
generationsToModel = 5

#Main menu function
def mainMenu():
    print("--------------------------------")
    print("1. Set Generation 0 Values")
    print("2. Display Generation 0 Values")
    print("3. Run The Model")
    print("4. Quit")
    print("--------------------------------")

    option = input("Select Option (1-5): ")

    if option == str(1):
        setValues()
    elif option == str(2):
        displayValues()
    elif option == str(3):
        runModel()
    elif option == str(4):
        quit()
    else:
        print("That is not an option!\n")
        mainMenu()

#Set values function
def setValues():
    try:
        popNumJuv = int(input("Set the population number for Juviniles: "))
        popNumAdults = int(input("Set the population number for Adults: "))
        popNumSen = int(input("Set the population number for Seniles: "))

        survNumJuv = float(input("Set the survival rate for Juviniles: "))
        survNumAdults = float(input("Set the survival rate for Adults: "))
        survNumSen = float(input("Set the survival rate for Seniles: "))

        birthRate = float(input("Set the birth rate: "))
        generationsToModel = int(input("Set the number of generations to model: "))
        mainMenu()
    except Exception:
        print("Failed to set values!")
        print("Returning to main menu...")
        mainMenu()

#Display values function
def displayValues():
    try:
        print("Juvinile Population Number: " + str(popNumJuv))
        print("Adult Population Number: " + str(popNumAdults))
        print("Senile Population Number: " + str(popNumSen))
        print("\n")
        print("Juvinile Survival Rate: " + str(popNumJuv))
        print("Adult Survival Rate: " + str(popNumAdults))
        print("Senile Survival Rate: " + str(popNumSen))
        print("\n")
        print("Birth Rate:" + str(birthRate))
        print("Number Of Generations To Model: " + str(generationsToModel))
        print("\n")
        mainMenu()
    except Exception:
        print("FAILED!")

#Run model function
def runModel():
    global popNumJuv, popNumAdults, popNumSen
    global survNumJuv, survNumAdults, survNumSen
    global birthRate
    print("\n")

    total = popNumJuv + popNumAdults + popNumSen

    firstPart = "GEN: 0" + "  |  " + "JUVINILE: " + str(popNumJuv) + "  |  " + "ADULT: " + str(popNumAdults)
    print(firstPart + "  |  " + "SENILE: " + str(popNumSen) + "  |  " + "TOTAL: " + str(total))

    time.sleep(1) #This time.sleep is not essential, I added it in to give the model a certain look to it

    for i in range(generationsToModel):
        newJuv = popNumAdults * birthRate
        newAdults = popNumJuv * survNumJuv
        newSen = (popNumAdults * survNumAdults) + (popNumSen * survNumSen)

        popNumJuv = newJuv
        popNumAdults = newAdults
        popNumSen = newSen

        total = popNumJuv + popNumAdults + popNumSen

        firstPart = "GEN: " + str(i + 1) + "  |  " + "JUVINILE: " + str(popNumJuv) + "  |  "

        print(firstPart + "ADULT: " + str(popNumAdults) + "  |  " + "SENILE: " + str(popNumSen) + "  |  " + "TOTAL: " + str(total))
        time.sleep(1) #This time.sleep is not essential, I added it in to give the model a certain look to it

#Main method that starts the program
if __name__ == "__main__":
    mainMenu()

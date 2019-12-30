#Import libaries
import time
import sys
import os

#Default generation values
popNumJuv = 10
popNumAdults = 10
popNumSen = 10

#Default survival rate values
survNumJuv = 1
survNumAdults = 1
survNumSen = 0

#Default birth rate, number of generations to model and total population values
birthRate = 2
generationsToModel = 5
total = 0

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
        generationsToModel = int(input("Set the number of generations to model (Between 5 and 25): "))

        if generationsToModel < 5 && generationsToModel > 25:
            print("\nThe number of generations must be between 5 and 25!")
            generationsToModel = int(input("Set the number of generations to model: "))

        mainMenu()
    except Exception:
        print("Failed to set values!")
        print("Returning to main menu...\n")
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
        mainMenu()

#Run model function
def runModel():
    global popNumJuv, popNumAdults, popNumSen
    global survNumJuv, survNumAdults, survNumSen
    global birthRate
    print("\n")

    #Generation 0 total population count
    total = popNumJuv + popNumAdults + popNumSen

    #The starting point for the model
    firstPart = "GEN: 0" + "  |  " + "JUVINILE: " + str(popNumJuv) + "  |  " + "ADULT: " + str(popNumAdults)
    print(firstPart + "  |  " + "SENILE: " + str(popNumSen) + "  |  " + "TOTAL: " + str(total))

    time.sleep(1) #This is not essential, I added it in to give the model a certain look to it

    #Try to run the model for X generations
    try:
        for i in range(generationsToModel):
            #Formula for calculating the population of greenfly
            newJuv = popNumAdults * birthRate
            newAdults = popNumJuv * survNumJuv
            newSen = (popNumAdults * survNumAdults) + (popNumSen * survNumSen)

            #Setting the original values to the new values
            popNumJuv = newJuv
            popNumAdults = newAdults
            popNumSen = newSen

            #Calculating the total number of greenfly
            total = popNumJuv + popNumAdults + popNumSen

            #I split these up because it was a very long line of code
            firstPart = "GEN: " + str(i + 1) + "  |  " + "JUVINILE: " + str(popNumJuv) + "  |  "
            print(firstPart + "ADULT: " + str(popNumAdults) + "  |  " + "SENILE: " + str(popNumSen) + "  |  " + "TOTAL: " + str(total))

            time.sleep(1) #This is not essential, I added it in to give running the model a certain look to it
    except Exception:
        print("ERROR! Could not run model.")
        mainMenu()

#Main method that starts the program
if __name__ == "__main__":
    mainMenu()

# Author : Avery Allison
# Date : November 2021
# Description : Final Project CSCI 141
# File : opGuesser.py
import random

# function name : calcAnswer
# parameters : listOps (list), listNums (list)
# returns : an integer
def calcAnswer(listOps, listNums) :
    # calculate the first part of the answer
    if (listOps[0] == "+") :
        answer = listNums[0] + listNums[1]
    elif (listOps[0] == "*") :
        answer = listNums[0] * listNums[1]
    elif (listOps[0] == "-") :
        answer = listNums[0] - listNums[1]

# calc second part of answer
    if (listOps[1] == "+") :
        answer = answer + listNums[2]
    elif (listOps[1] == "*") :
        answer = answer * listNums[2]
    elif (listOps[1] == "-") :
        answer = answer - listNums[2]
    return answer

# function name : getOperators
# returns : a list
def getOperators() :

    operators = []

    # generate random number that will pick operators
    seed1 = random.randint(0,2)
    seed2 = random.randint(0,2)

    # append operators list with operators
    if (seed1 == 0) :
        operators.append("+")
    elif (seed1 == 1) :
        operators.append("-")
    else :
        operators.append("*")
    if (seed2 == 0) :
        operators.append("+")
    elif (seed2 == 1) :
        operators.append("-")
    else :
        operators.append("*")
    return operators

# main function
def main() :

    numbers = []

    # tell user about the game and ask them how many tries they want
    print("This is a game where you pick three numbers and try and guess what operations were performed on them,\nand in what order.")
    inputTries = int(input("How many tries would you like? "))

    # ask user if they want to input from a file, or choose 3 numbers through input
    whereNums = input("Type 'file' to choose numbers from numbers.txt\nRETURN to enter numbers manually: ")
    if (whereNums == "file") :
        numbersFile = open("numbers.txt", 'r')
        for line in numbersFile :
            if ("Enter 3 numbers below, each one on a new line:" not in line) :
                numbers.append(int(line))
    else :
        numbers.append(int(input("Enter the first number: ")))
        numbers.append(int(input("Enter the second number: ")))
        numbers.append(int(input("Enter the third number: ")))

    # generate scrambled list of numbers
        
    random.shuffle(numbers)

    # generate operators to use
    randomOperators = getOperators()

    # print answer and prompt user to guess for each try
    for currentTry in range(0, inputTries) :
        guess = []
        print("The answer is " + str(calcAnswer(randomOperators, numbers)) + ", " + str(inputTries - currentTry) + " guess(es) left")
        guess.append(input("Guess the first operator: "))
        guess.append(input("Guess the seond operator: "))

# check if user is correct and respond accordingly
        if (str(guess) == str(randomOperators)) :
            break
        else :
            print("Incorrect combo, guess again")
# user loses if no tries or correct guess
    if (str(guess) == str(randomOperators)) :
        print("You guessed correctly, congratulations!")
    else :
        print("You ran out of tries, sorry!")
        print("operators: " + str(randomOperators))
        print("number order: " + str(numbers))

main()
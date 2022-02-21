# Amir Ahsan
# Module 4 Assignment

from sys import exit
from random import randint

#Start Here
#Place comment here
"""
here is a block quote comment
these can be multi-line
"""

#creates a dictionary called myData
myData = {}
#creates a variable called guess initialized to 0
guesses = 0
#creates a variable called wins initialized to 0
wins = 0

#open and read/display file named questions.txt
with open("questions.txt", "r") as infile:
#variable to hold input values from user
    questions = infile.readlines()
#loop that runs 
    for question in questions:
#loop that runs if line contains first then input into mydata dictionary as first name
            if "first" in question:
#insert user input as first name into myData
                myData["first_name"] = input(question)
#loop thats runs if line contains last then input into mydata dictionary as last name
            elif "last" in question:
#inster user input as last name in myData                
                myData[" last_name"] = input(question)
#end if loop since it does not contain the words first or last in line
            else:
#print to screen letting user know next line in questions file is not wrong
                print("bad questions in input file")
#exit for loop
                exit()
#for loop that runs as long as play is in 0-10 range
for play in range(10):
#initialize a variable "number" which is a random integer between 1 and 100
    number = randint(0, 100)
#intialize solver as a boolean currently set to False    
    solved = False
#below while loop runs as long as solved is false
    while not solved:
#guess variable holds a integer input from user
        guess = int(input(f"Guess a number from 0 to 100 : "))
#increase the value of the variable guesses by 1
        guesses += 1
#loop to run if the guess is the same as the random integer number        
        if guess == number:
#prints successful message with username originally entered
            print(f"Great Job, your guess of {guess} is correct")

#variable win is incremented by 1 amd is the new value of win
            wins += 1
#boolean variable solved is now set to True
            solved = True
#break out of this if loop and return to while loop which now will read value of solved as True
            break
#loop to run if the guess variable is not equal to the random int variable number        
        if guess != number:
#print unsuccessful statement            
            print (f"Your guess of {guess} is incorrect!")
#loop if the guess variable value is higher than the random variable value number
        if guess > number:
#print message letting user know that input number was higher than the random integer
            print(f"Sorry, you guessed too high!!")
#else if loop statement that runs if the guessed value is lower than the random integer value
        elif guess < number:
#print message letting user know that input number was lower than the random integer        
            print(f"Sorry, you guessed too low!!")
#else statement to end if loops
        else:
#exit statment to end loop without error            
            pass
#if loop if solved value is true
    if solved:
#statement letting user know how many times correctly guessed         
        print(f"Lets play again, you have completed {wins} out of 10 plays.")
#statement to exit from loop completely
        continue

#statement to show many correctly guessed outcomes by user
print(f"guessed the correct number {wins} out of 10 plays.")
#second statement to how many times played game to get 10 wins
print(f"It took  {guesses} guesses to do this!")

        
            
        

        
            
        

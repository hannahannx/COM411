#importing modules
import random

def run ():
  #Asking the use to selected a max and min values
  minimum = int(input("Please enter the minimum value"))
  maximum = int(input("Please enter the maximum value"))
  #allocating a random number to be tested to
  random_num = random.randrange(minimum,maximum)
      
  #setting a local varible
  answer = False 
  #Asking the user to guess the correct answer, until they get it correct
  while answer == False :
    #Asking for user input
    guess = int(input("I am thinking of a number between {} and {}. Can you guess what it is?".format(minimum,maximum)))
    #comparing the guess the the random number to be chosen
    if guess < random_num:
      print("Your guess is too low.")
      print("Try again")
    elif guess > random_num:
        print("Your guess is too high.")
        print("Try again")
    else:
      #stoping the loop by changing the local variable
      print("Congratulations! You guessed my number!")
      answer = True

run()

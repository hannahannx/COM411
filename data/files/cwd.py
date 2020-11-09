#importing the os module
import os
#Creating a function
def cwd():
  #returning the current directory
  path = os.getcwd()
  print("The current working directory is {}".format(path))
  print("The directory contains the following:")
  #Printing out the directories line by line using a loop
  for file in os.listdir(path):
    print(file)

#Creating a funcion to executee the program
def run ():
  print("Processing...")
  cwd()

#Runnning the main program
run()
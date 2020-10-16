#defining function to print simple word
def box (word):
  print("|_",word,"_|)")

#defining function to print the word in lowercase
def lowercase (word):
  new_word = word.lower()
  print(new_word)

#defining function to print the word in upper case
def uppercase (word):
  new_word = word.upper()
  print(new_word)

#defining function to print tthe word to flip the order it will be printed in
def mirrored(word):
  new_word = word[::-1]
  print(new_word)

#defining function to print the word reversing lower and upper case for the number of times that the user has requested
def repeating(word):
  #Asking the user how many times they want the alterantion to be done
  repeat = int(input("How many times would you like this word to be repeated?"))
  #printing the upper and lower case based on the times they've asked to repeat
  for repeats in range(repeat):
    upper = word.upper()
    lower = word.lower()
    print(lower)
    print(upper)

#defining a function to run the whole program
def run():
  #asking the user for an input
  word = str(input("Please enter a word: "))
  #asking the user for the options on what they would like to do in the program
  options = str(input("What would you like to do next?\n a)Display in a box \n b) Dispay lowercase \n c)Display uppercase \n d)Display mirrored \n e)Repeat \n Please select ONE: "))
  #routing the user to the different possiblities of the program
  if options == "a":
    print(box(word))
  elif options == "b":
    print(lowercase(word))
  elif options == "c":
    print(uppercase(word))
  elif options == "d":
    print(mirrored(word))
  elif options == "e":
    print(repeating(word))
  else:
    print("You have not selected an valid option.")

#Calling the main program
run()
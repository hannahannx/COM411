def run(:)
  #Printing out the starting message an creating the message
  print("Program Started!")
  character = str(input("Please enter a standard character."))

  if (len(character) == 1):
    print("The ASCII code for the letter {} is: {}".format(character,ord(character)))
  else:
    print("You have not entered a character. ")

    print("Program Ended")

run()


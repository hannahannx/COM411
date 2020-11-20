
def run():
  #This will be a code to demonstrate the use of decisions,nesting and logical operators
  # I will be making a quiz on 3 differemt subjects
  # These subjects will be Maths, English and Biology

  #Main Program

  #Displaying the menu screen with the options of what subjects that they would like to be tested on
  # Displaying the Main Menu
  print("Hi! Welcome to the knowledge quiz!")
  print()
  #Intialising global varibles
  correct = 0
  name = str(input("What is your name?"))
  subject_options = str(input("What subject would you like to be tested on today? \n a) Maths \n b) EXIT \n Please choose ONE option: "))
  print()
  #Choosing the options
  if subject_options == "a":
  #Displaying the Maths Questions
    print("Welcome to the Maths Quiz {}!".format(name))
    maths_options = str(input("What topic in maths would you like to be tested on? \n a) Addition  \n b)Subtraction \n Please chose ONE option: "))
    if maths_options == "a":
      print("Welcome to the Addition quiz {}!".format(name))
      q1 = int(input("5 + 5 ="))
      q2 = int(input("94 + 6 ="))
      q3 = int(input("10 + 38 ="))
      q4 = int(input("1 + 38 = "))
      q5 = int(input("833 + 23 ="))
      if q1 == 10:
        correct = correct + 1
      if q2 == 100:
        correct = correct + 1
      if q3 == 48:
        correct = correct + 1
      if q4 == 39:
        correct = correct + 1
      if q5 == 856:
        correct = correct + 1
      print("You have got {} questions correct.".format(correct))
      print("END OF QUIZ-----------------------------------")
    elif maths_options == "b":
      print("Welcome to the Subtraction quiz {}!".format(name))
      q1 = int(input("5 - 5 ="))
      q2 = int(input("94 - 6 ="))
      q3 = int(input("10 - 38 ="))
      q4 = int(input("1 - 38 = "))
      q5 = int(input("833 - 23 ="))
      if q1 == 0:
        correct = correct + 1
      if q2 == 88:
        correct = correct + 1
      if q3 == -28:
        correct = correct + 1
      if q4 == -37:
        correct = correct + 1
      if q5 == 810:
        correct = correct + 1
      print("You have got {} questions correct.".format(correct))
      print("END OF QUIZ-----------------------------------")
    elif maths_options == "c":
      print("Welcome to the Multiplication quiz {}!".format(name))
      q1 = int(input("5 x 5 ="))
      q2 = int(input("6 x 4 ="))
      q3 = int(input("12 x 9 ="))
      q4 = int(input("33 x 2 = "))
      q5 = int(input("3 x 13 ="))
      if q1 == 25:
        correct = correct + 1
      if q2 == 24:
        correct = correct + 1
      if q3 == 108:
        correct = correct + 1
      if q4 == 66:
        correct = correct + 1
      if q5 == 39:
        correct = correct + 1
      print("You have got {} questions correct.".format(correct))
      print("END OF QUIZ-----------------------------------")
    else:
      print("You have not selected the options that I have given you, Goodbye {}".format(name))
  #Exiting the program
  elif subject_options == "b":
    print("You have selected to exit the program, Goodbye {}".format(name))

  else:
    print("You have not selected the options I have given you, Goodbye {}".format(name))

run()
    
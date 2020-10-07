#This will be a code to demonstrate the use of decisions,nesting and logical operators
# I will be making a quiz on 3 differemt subjects
# These subjects will be Maths, English and Biology

#Main Program

#Displaying the menu screen with the options of what subjects that they would like to be tested on
# Displaying the Main Menu
print("Hi! Welcome to the knowledge quiz!")
print()
correct = 0
name = str(input("What is your name?"))
subject_options = str(input("What subject would you like to be tested on today? \n a) Maths \n b) English \n c) Biology \n Please choose ONE option: "))
print()

if subject_options == "a":
# Displaying the Maths Questions
  print("Welcome to the Maths Quiz {}!".format(name))
  maths_options = str(input("What topic in maths would you like to be tested on? \n a) Addition  \n b)Subtraction  \n c)Multiplication \n Please chose ONE option: "))
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

  elif maths_options == "c":
    print("Welcome to the Multiplication quiz {}!".format(name))
  else:
    print("You have not selected the options that I have given you, Goodbye {}".format(name))

# Displaying the English Questions
elif subject_options == "b":
  print("Welcome to the English Quiz{}!".format(name))

# Displaying the Biology Questions
elif subject_options == "c":
  print("Welcome to the Biology Quiz{}!".format(name))

else:
  print("You have not selected the options I have given you, Goodbye {}".format(name))
  
def run():
  #This is my code in which it will be tracking the mood, bmi and dialogue of the user. It will:
  #Store their name, height, weight (and convert it into BMI), and mood
  print("Hi! Welcome to your day diary!")
  #Making the variables 
  name = str(input("Please enter your name"))
  print("Your name is",name,"is this correct?")
  confirm = str(input("Please enter Y - Yes or N - No"))

  if confirm == "Y":
    print("Welcome to your diary",name,"!")
    #Letting the user choose what they would like to do today
    track = int(input("What would like to track today? 1 - Weight and Height, 2 - Mood, "))
    if track == 1:
      height = float(input("How tall are you (in meters"))
      weight = float(input("How much do you weigh in kilograms?"))
      bmi = weight / (height**2)

      print("Your current bmi is ,",bmi)
    elif track == 2:
      mood = int(input("What would you rate your mood today out of 5"))
      if mood > 5:
        print("That is not a valid number on the scale.")

      print("Your mood is:")
      print("♥" * mood,"out of ♥♥♥♥♥")
    else:
      print("You have not selected one of the available options")  
  elif confirm == "N":
    #exiting the program
    print("Okay, bye")
  else:
    #exiting the program
    print("You have not selected one of the available options.")
    
run()
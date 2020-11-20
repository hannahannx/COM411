def run():
  #Creating the varible to ask the activity
  activity = str(input("Please enter the activity to be performed."))
  #Creating the branches for the type of statement to be printed out
  if (activity.lower() == "calculate"):
    print("Performing calculations...")
  else:
    print( "Performing activity...")

  print("Activity completed!")
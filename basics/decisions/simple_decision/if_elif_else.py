def run():
   #Creating the varibles for the direction
  direction = str(input("Towards which direction should I paint (up, down, left or right)?"))
  #Creating the branches to show which direction the robot will be painting in
  if (direction == "up"):
    print("I am painting in the upward direction!")
  elif (direction == "down"):
    print("I am painting in the downward direction")
  elif (direction == "left"):
    print("I am painting in the left direction")
  elif (direction == "right"):
    print("I am painting in the right direction")
  else:
    print("You  have not selected any of the avaiable options..")

run()
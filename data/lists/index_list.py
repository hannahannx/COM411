#Defining a fuction
def movements ():
  #Creating a list
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  #printing the list
  return path

#Defininf a function to run the program
def run():
  print("Moving...")
  path = movements()
  print("{} for {} steps".format(path[0],path[1]))
  print("{} for {} steps".format(path[2],path[3]))
  print("{} for {} steps".format(path[4],path[5]))
  print("{} for {} steps".format(path[6],path[7]))

#Calling the program 
run()


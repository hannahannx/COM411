#Defining a function to create a list and return the values of the list
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

#Creating a function to show a menu screen by using a loop
def menu():
  print("PLease select a direction")
  #Creates a new varible to assign  the list in the previous function 
  direct = directions()
  for index in range (0,len(direct)):
    print("{} : {} ".format(index,direct[index]))
  user_direction = int(input())
  print()
  return direct[user_direction]

#Creating a function to run the program
def run():
  print("Working out escape route...")
  route = []
  for i in range(0,5,1):
    route.append(menu())
  print("Escape route: {}".format(route))

#Calling the program 
run()
def run():
  #Creating user input
  steps =int(input("How many steps are we from the cave? "))
  #Creating loop printing out based on user input
  for step in range(steps,0,-1):
    print("{} steps remaining".format(step))
  #Ending the loop and printing final message
  print("We have reached the cave!")

run()
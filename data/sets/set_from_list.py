#Defining  a function
def observed ():
  #Creating a list based on user input
  observations = []

  #Asking the user of places 7 times
  for place in range(0,7,1):
    observation = str(input("Please enter an observation: "))
    #adding the plaes after each iteration
    observations.append(observation)
  return observations

#Defining a function to run the program
def run():
  print("Counting observations...")
  observations = observed()
  #Creating a set that will contain a tuple for each of the unqie values in the list
  observations_set = set()
  #For every observation that is in the set, count how many time the unqiue value is inputed 
  for observation in observations:
    observations_set.add((observation,observations.count(observation)))
  #printing out the observation status
  print("{} observed {} times".format(observation,observations.count(observation)))
  
#Running the main program by calling the run function
run()

  
  

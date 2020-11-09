#Defining  a function
def observed ():
  #Creating a list based on user input
  observations = []

  #Asking the user of places 5 times
  for place in range(0,5,1):
    observation = str(input("Please enter an observation: "))
    #adding the plaes after each iteration
    observations.append(observation)

  return observations

def remove_observations(observations):
  #preparing for a loop
  remove = True
  #Looping askng the question
  while remove == True:
    question = str(input("Would you like to remove observations?\n a) YES \n b) NO \n"))
    if question.lower() == "a":
      observation_to_remove = str(input("What observation would you like to remove? "))
      observations.remove(observation_to_remove)
      print("Done!")
      print("New list of observations: {}".format(observations))
    else:
      remove = False

def run():
  #Making sure that the values from the prefvious function can be accessed
  all_observations = observed()
  remove_observations(all_observations)

  # populate set
  observations_set = set()
  for observation in all_observations:
    data = (observation, all_observations.count(observation))
    observations_set.add(data)

  # display set
  for data in sorted(observations_set):
    print("{} observed {} time(s).".format(data[0],data[1]))

run()

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

def remove_observations(all_observations):
  question = str(input("Would you like to remove observations?\n a) YES \n b) NO \n"))
  if question.lower() == "a":
    remove = True
    while remove == True:
      observation_to_remove = str(input("What observation would you like to remove? "))


  
  
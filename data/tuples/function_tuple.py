#Defining a function to return the smallest likelihood
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  #min = minimum
  return (min(likelihoods)), (max(likelihoods))

#Defining a function to run the program
def run():
  percentages = likelihood()
  print("Minimum likelihood of falling: {}%".format(percentages[0]))
  print("Maximum likelihood of falling: {}%".format(percentages[1]))

#Calling the functions
run()
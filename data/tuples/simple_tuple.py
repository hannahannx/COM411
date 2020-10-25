#Defining a function to return the smallest likelihood
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  #min = minimum
  return (min(likelihoods))

#Defining a function to run the program
def run():
  minimum_value = likelihood()
  print("Minimum likelihood of falling: {}%".format(minimum_value))

#Calling the functions
run()
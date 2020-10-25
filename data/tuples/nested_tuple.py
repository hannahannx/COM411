#Defining a function
def steps():
  likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods 

#Defining the function to run the program
def run():
  step = steps()
  good_steps = []
  bad_steps = []

  for index in step:
    if index[1] >= 50:
      bad_steps.append(index)
    else:
      good_steps.append(index)
  print("Good Steps: {}, Bad Steps, {}".format(len(good_steps),len(bad_steps)))

  #Running the program
  run()
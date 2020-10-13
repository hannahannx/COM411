#defining a function
def climb_ladder(number_of_steps_remaining,number_of_steps_crossed):
  #Compare the values of the two parameters to print out a message
  if number_of_steps_remaining > number_of_steps_crossed :
    print("Still some way to go!")
  else:
    print("We are almost there!")

#calling the function
climb_ladder(5,2)
climb_ladder(2,5)
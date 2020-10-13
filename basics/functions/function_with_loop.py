#defining a function
def cross_bridge(distance_in_steps):
  #priniting out a message per each step there is 
  for message in range(distance_in_steps):
    print("Crossed Step")
  #printintg a message at the end of the loop depending on the amount of steps
  if distance_in_steps >= 5 :
    print("The bridge is collapsing")
  else:
    print("We must keep going")

#calling the function
cross_bridge(3)
cross_bridge(6)


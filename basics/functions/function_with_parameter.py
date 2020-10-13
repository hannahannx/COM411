#defining a function
def escape_by(plan):
  #deciding on what to output based on the user input
  if plan.lower() == "jumping over":
    print("We cannot escape that way! The bouder is too big")
  elif plan.lower() == "running around":
    print("We cannot escape that way! The boulder is moving too fast!")
  elif plan.lower() == "going deeper":
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

#calling the fucntion with parameters
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")  
#Creating a fucntion 
def short_pattern ():
  pattern = {"sequence":"101","occurrences":5}
  return pattern

#Creating a fucntion
def medium_pattern ():
  pattern = {"sequence":"111000","occurrences": 25}
  return pattern

#Creating a fucntion 
def long_pattern ():
  pattern = {"sequence":"1100110011001100","occurrences":50}
  return pattern

#Creating a fucntion to run the whole program
def run():
  print("Analysing patterns...")
  all_patterns = {
    "short sequence":short_pattern(),
    "medium sequence": medium_pattern() ,
    "long sequence": long_pattern()
  }

  for key,value in all_patterns.items():
    print("{} : {}".format(key,value))

run()



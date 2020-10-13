#'defining a function'
def sum_weights(beep_weight,bop_weight):
  #calculating the total weight of beep and bop
  total_weight = beep_weight + bop_weight
  #returning the total weight
  return total_weight

#defining a function
def calc_avg_weight(beep_weight,bop_weight):
  #calculating the avergae weight and returning it
  avg_weight = sum_weights() / 2
  return avg_weight

#Defining function to run the program
def run():
  #asking fr user input
  beep_weight = int(input("What is the weight for Beep?"))
  bop_weight = int(input("What is the weight for Bop?"))
  option = str(input("What would you like to calculate (sum or average)?"))
  #asking what they want to calculate
  if option.lower() == "sum":
    print("The sum of Beep and Bop's weight is {}".format(sum_weights(beep_weight,bop_weight)))
  elif option.lower() == "average":
    print("The average of Beep and Bop's weight is {}".format(calc_avg_weight(beep_weight,bop_weight)))
  else:
    print("You did not selection sum or average.")

#Calling the function to run the program
run()
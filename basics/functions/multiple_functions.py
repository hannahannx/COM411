#defining a function 
def display_ladder(steps):
  #prints out the ascii ladder for the number of steps printed
  for ladder in range(steps):
    print("| |")
    print("***")

#defining a function
def create_ladder():
  #asking for user input
  number_of_steps = int(input("How many steps remain?"))
  #print out the ladder in total by callng the display_ladder function
  display_ladder(number_of_steps)

#calling the function
create_ladder()
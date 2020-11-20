def run():
  #Creating user input varibles
  bars = int(input("How many bars should be charged: "))
  print()
  #Craeting a counter
  current_bars = 0
  #Creating the loop to print the bars 
  while current_bars != bars:
    print("Charging:", end="") # Makes sure it prints on the same line
    current_bars = current_bars + 1
    print(" █ " * current_bars)
  #Printing out final message
  print("The battery is fully charged.")

run()
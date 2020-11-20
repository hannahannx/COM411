def run():  
  #Waiting for user input
  number = int(input("Please enter a number: "))
  #setting  global variable
  counter = 0
  total = 1
  # Calculate factorial
  while counter < number:
      counter = counter + 1
      total = total * counter
  print("The factorial is", total)

run()
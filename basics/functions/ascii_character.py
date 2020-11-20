def run():
  #Printing the starting message and creating user input varible
  print("Program Started!")
  ascii_code = int(input("Please enter an ASCII code."))

  #Checking if the user input is a positive integer
  if (ascii_code < 0):
    ascii_code = abs(ascii_code)

  #checking to see if th values are in range
  if ascii_code in range(33, 127):
    convert = chr(ascii_code)
    print("The character represented by the ASCII code {} is {}." .format(ascii_code,convert))
  else:
    print("You have not entered a value within range")
  #ending the program
  print("Program Ended!")

run()
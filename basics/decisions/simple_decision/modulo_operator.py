#Creating a variable for the whole number
whole_number = int(input("Please enter a whole number"))
#Creating the branches for the odd and even numbers 
if (whole_number % 2) != 0:
  print("The number",whole_number,"is an odd number")
else:
  print(whole_number,"is an even number")
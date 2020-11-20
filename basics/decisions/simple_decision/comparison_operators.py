def run():
  #CReating the variables
  num1 = int(input("Please enter the first number"))
  num2 = int(input("Please enter the second number"))
  #Creating the comparison betweeen the two numbers
  if num1 > num2:
    print("The second number is the smallest")
  elif num2 > num1:
    print("The first number is the smallest")
  else: 
    print("Both are equal!")

run()
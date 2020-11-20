def run():  
  #Creating the varibales
  num1 = int(input("Please enter the first whole number."))
  num2 = int(input("Please enter the second whole number."))
  num3 = int(input("Please enter the third whole number."))
  #Global varibales
  even = 0
  odd = 0
  #Creating the decisons for the even and odd numbers
  if (num1 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  if (num2 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  if (num3 % 2) == 0:
    even = even + 1
  else:
    odd = odd + 1

  print("There were",even,"even and",odd,"odd numbers!")

run()
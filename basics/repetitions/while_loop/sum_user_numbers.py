def run():
  #Creating user input
  sum = int(input("How many numbers should I sum up?"))
  #initalising counter variables
  sum_count = 0
  answer = 0
  #Asking for the values
  while sum_count != sum:
    repeat = int(input("Please enter number {} of {}: ".format(sum_count+1,sum)))
    sum_count = sum_count + 1
    answer = answer + repeat
  #Printing 
  print("The answer is {}.".format(answer))

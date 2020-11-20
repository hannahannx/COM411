def run():
  #Creating user input and print statement
  markings = str(input("What strange markings fo you see?"))
  print()
  print("Identifying...")
  print()
  #Creating the loop to print out them individually
  for line in range(0,len(markings),1):
    print("index {}: ".format(line),markings[line])
  #printing the finished code
  print()
  print("Done!")

run()
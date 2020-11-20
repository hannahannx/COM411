def run():
  #Adking the user for user input
  sequence = str(input("Please enter a sequence: "))
  print()
  marker = str(input("Please enter the character for the marker: "))
  print()
  #Creating the markers
  marker1 = 0
  marker2 = 0
  #Finding the markers
  for find in range(0,len(sequence),1):
    marks = sequence[find]
    #Looking for the marker in the sequence
    if marks == marker :
      marker1 == find
    else:
      marker2 = find

  #calulating the difference in markers
  difference = marker2 - marker1
  #printing out the result
  print("The disatnce between the markers is {}".format (difference))

run()
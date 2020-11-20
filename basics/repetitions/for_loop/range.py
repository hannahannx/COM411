def run():
  #Creating user input
  brightness = int(input("What level of brightness is required? "))
  print("Adjusting brightness...")
  #Creating the for loop 
  for level in range(2,(brightness+2),2):
    print("Beep's brightness level: {}".format("*" * level))
    print("Bop's brightness level: {}".format("*" * level))
    print()
  print("Adjustments complete!")

run()

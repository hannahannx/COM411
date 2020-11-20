def run():
  #Creating user input variables
  live_cables = int(input("How many cables show I remove: "))
  print()
  #Creating counter variable
  removed_live_cables = 0
  #Continuing to remove he cabes fr the amount of cabes requested in the user input
  while removed_live_cables != live_cables:
    print("Avoiding...",end ="")
    removed_live_cables = removed_live_cables + 1
    print("...Done! {} live cable avoided!".format(removed_live_cables))
  print("All live cables have been avoided.")

run()

def run():
  lives = int(input("Please enter the number of lives"))
  energy = int(input("Please enter the energy level."))
  shields = int(input("Please enter the shield level."))

  print("Health has been set.")
  print("Lives:")
  print ("♥" * lives)
  print("Energy:")
  print("♦" * energy)
  print("Shield:")
  print("♦" * shields)

run()

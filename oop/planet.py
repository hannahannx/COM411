class Planet:
  #initalising class
  def __init__(self):
    self.humans = []
    self.robots = []

  def add_human(self,human):
    self.humans.append(human)
    
  def remove_human(self,human):
    self.humans.remove(human)

  def add_robot(self,robot):
    self.robots.append(robot)

  def remove_robot(self,robot):
    self.robots.remove(robot)

  def __repr__(self):
    return ("This is a list of robots: {}\nThis is the list of humans {}".format(self.robots,self.humans))

  def __str__(self):
    return ("robots = {}\nhumans =  {}".format(self.robots,self.humans))
  
#outputting the code
if (__name__ == "__main__"):
  planet = Planet()
  human = input("What human would you like to add")
  robot = input("What robot would you like to add?")
  print("Adding Human....")
  planet.add_human(human)
  print(repr(planet))
  print(str(planet))
  print("Removing Human...")
  planet.remove_human(human)
  print(repr(planet))
  print(str(planet))
  print("Adding Robot...")
  planet.add_robot(robot)
  print(repr(planet))
  print(str(planet))
  print("Removing Robot...")
  planet.remove_robot(robot)
  print(repr(planet))
  print(str(planet))
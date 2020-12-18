#importing modules
import random
import matplotlib.pyplot as plt

class Planet:
  #initalising class
  def __init__(self):
    self.inhabitants = {'humans' : [], 'robots' : []}
    
  def add_human(self,human):
    self.inhabitants['humans'].append(human)
    
  def remove_human(self,human):
    self.inhabitants['humans'].remove(human)

  def add_robot(self,robot):
    self.inhabitants['robots'].append(robot)

  def remove_robot(self,robot):
    self.inhabitants['robots'].remove(robot)

  def __repr__(self):
    return ("This is a dictionry of inhabitants: {}".format(self.inhabitants))

  def __str__(self):
    return ("robots = {}\nhumans =  {}".format(self.inhabitants['robots'],self.inhabitants['humans']))

class Universe:
  def __init__(self):
    self.allPlanets = []
  
  def generate(self):
    newPlanet = Planet()
    self.randomNumbers = random.randint(1,10)
    self.randomNumbers2 = random.randint(1,10)
    #random amount of humans to planet
    for i in range(self.randomNumbers):
      print("{} generated".format(i+1))
      human = input("What human would you like to add")
      print()
      newPlanet.add_human(human)
      self.allPlanets.append(newPlanet)
    #random amount of robot to planet
    for j in range(self.randomNumbers2):
      print("{} generated".format(j+1))
      robot = input("What robot would you like to add?")
      print()
      self.allPlanets = newPlanet
      newPlanet.add_robot(robot)

      
    print(self.allPlanets)
    return newPlanet

  def show_populations(self):
    total = Universe.generate(planet)
    fig, ax = plt.subplots()
    counthuman = len(total)
    humanx = range(1,20)
    humany = counthuman
    ax.bar(humanx,humany,"m")

    countrobot = len(self.allPlanets[0])
    robotx = range(1,20)
    roboty = countrobot
    ax.bar(robotx,roboty,"b")
    plt.show()



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

  Universe.generate(planet)
  Universe.show_populations(planet)


  
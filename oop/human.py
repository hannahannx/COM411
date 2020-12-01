class Robot:
  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)
  
  #Human attribute -constant in caps
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
    self.energy = Robot.MAX_ENERGY
  
  #increasing the age by 1
  def grow(self):
    self.age = self.age + 1

   #increasing the energy
  def eat(self,amount):
    if amount < self.energy:
      self.energy = self.energy + amount
    else:
      print("You cannot do that as the amount {} is greater than the current energy {} ".format(amount,self.energy)) 

  #reducing the engery
  def move(self,distance):
    if self.energy >= 0:
      self.energy = self.energy - distance
    else:
      print("You cannot decrease it by this ammount")

  # An instance method
  def __repr__(self):
    return ("Robot:My name is {} and I am {} years old my current energy is {}".format(self.name,self.age,self.energy))
  


class Human:
  #Human attribute -constant in caps
  MAX_ENERGY = 100

  #Initalising the class
  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  #increasing the age by 1
  def grow(self):
    self.age = self.age + 1

  #increasing the energy
  def eat(self,amount):
    if amount < self.energy:
      self.energy = self.energy + amount
    else:
      print("You cannot do that as the amount {} is greater than the current energy {} ".format(amount,self.energy)) 
  
  #decreasing the energy
  def move(self,distance):
    if self.energy >= 0:
      self.energy = self.energy - distance
    else:
      print("You cannot decrease it by this ammount")

  #Showing the name for that specific object to be made
  def __repr__(self):
    return ("Human: My name is {} and I am {} years old my current energy is {}".format(self.name,self.age,self.energy))

#creating a object to display the code above 
if (__name__ == "__main__"):
  human = Human()
  robot = Robot()
  print(repr(human))
  print(repr(robot))
  human.grow()
  robot.grow()
  print(repr(human))
  print(repr(robot))
  human.move(3)
  robot.eat(3)
  print(repr(human))
  print(repr(robot))
  human.eat(200)

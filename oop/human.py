class Robot:
  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
class Human:
  #Human attribute -constant in caps
  MAX_ENERGY = 100

  #Initalising the class
  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  #Showing the name for that specific object to be made
  def display(self):
    print("I am {}".format(self.name))

#creating a object to display the code above 
if (__name__ == "__main__"):
  human = Human()
  human.display()
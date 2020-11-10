#importing module
import matplotlib.pyplot as plt

#Creating a function to return the values inputted by the user
def coordinate():
  x = int(input("Please enter a x value: "))
  y = int(input("Please enter a y value: "))
  return (x, y)

#Creating a function
def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for value in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]

#Creating a function to run the program
def run():
  values = path()
  plt.plot(values[0],values[1],"-")
  plt.show()

#Running main program
run()

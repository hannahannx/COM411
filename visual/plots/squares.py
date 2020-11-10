#importing the libary
import matplotlib.pyplot as plt

#creating a function for small
def small():
  x_values = [3,4,4,3,3]
  y_values = [3,3,4,4,3]
  plt.plot(x_values,y_values,'ro:')

#creating a function for small
def medium():
  x_values = [2,2,5,5,2]
  y_values = [2,5,5,2,2]
  plt.plot(x_values,y_values,'gs--')

#creating a function for small
def large():
  x_values = [0,0,6,6,0]
  y_values = [0,6,6,0,0]
  plt.plot(x_values,y_values,'bo-')

#CReating a function to run the program
def run():
  small()
  medium()
  large()
  plt.show()

#Main program
run()

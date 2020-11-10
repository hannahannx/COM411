#importing the libary
import matplotlib.pyplot as plt

#Creating a function to plot the values of x and y
def display(x,y):
  plt.plot(x,y)
  plt.show()

#Creating a function to run 
def run():
  x_values = [1,2,3,4,5]
  y_values = [1,4,9,16,25]
  display(x_values,y_values)

#Main program
#execution
run()
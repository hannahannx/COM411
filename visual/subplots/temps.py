#importing  the module 
import matplotlib.pyplot as plt

#Creating a function
def read_data(fileName):
  #opens file
  with open(fileName) as textFile:
    temps = []
    #reads each line and returns the data in temps
    for line in textFile:
      temps.append(float(line.strip()))
    return temps

#Creating a function
def run():
  data = read_data("visual/subplots/temps.txt")
  #making 1 row and 2 graphs 
  fig, axes = plt.subplots(1, 2)

#making the x and y vaues
  x = range(1,8)
  y = data

#prints out  line grapgh and bar chart with the temperartures
  axes[0].plot(x, y)
  axes[1].bar(x, y)
   
  #making the layout fit on the page
  plt.tight_layout()
  plt.show()

run()

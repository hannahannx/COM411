#importing  the module 
import matplotlib.pyplot as plt

#Creating a function
def read_data(fileName):
  #opens file
  with open(fileName) as textFile:
    #reads each line and returns the data
    for line in textFile:
      temps = []
      temps.append(line.strip())
    return temps
    print(temps)

#Creating a function
def run():
  data = read_data("visual/subplots/temps.txt")
  fig, axes = plt.subplots(1, 2)
  x = range(7)
  y = data  

  axes[0].plot(x, y)
  axes[1].bar(x, y)
   
  plt.tight_layout()
  plt.show()

run()

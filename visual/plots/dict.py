#importing module
import matplotlib.pyplot as plt
import random

#Craeting a function
def data():
  paths = {}
  lineType = input("What type of line  would you like? (dotted - :, dashed - -- or solid - -)")
  colourType = input("What type of colour  would you like? (red - r, green - r or blue - b)")
  markerStyle = input("What marker style woud you like? (circle - o square - s or triangle - ^)")
  #Adding elements to the dictionary
  paths['lineType'] = lineType
  paths['colourType'] = colourType
  paths['markerStyle'] = markerStyle

  return paths

def generate():
  linesToPrint = int(input("How many lines would you like to display? "))
  for line in range(linesToPrint):
    values = data()
    #Generate 5 random numbers between 1 and 10
    x = random.sample(range(1,10,),5)
    y = random.sample(range(1,10),5)
    format = f"{values['colourType']}{values['lineType']}{values['markerStyle']}"
    plt.plot(x,y,format)
    plt.show()

def run():
  print("Running...",end="")
  generate()
  print("Done!)")


run()

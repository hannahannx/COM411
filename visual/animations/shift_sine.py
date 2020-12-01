#importing modules 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#Making the subplots to animate the figure
fig, ax = plt.subplots()

#Creating function to animate the graph
def animate(frame):
  #only showing the current plot
  ax.cla()
  #Setting the highest and lowest values possible for x and y
  ax.set_xlim(0,2*np.pi) #2*np.pi= 2pi written in this format
  ax.set_ylim(-1,1)
  x = np.arange(0,(2*np.pi), 0.01)
  #calculating the movement of the graph
  y = np.sin(x + frame/50)
  ax.plot(x,y, "m")

def run():
  some_animation = animation.FuncAnimation(fig, animate, frames =720 ,interval=100)
  print(some_animation)
  plt.show()

run()
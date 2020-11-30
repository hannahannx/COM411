#importing modules 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#Making the subplots to animate open
fig, ax = plt.subplots()

#Creating a fuction to animate the axes
def animate(frame):
  #setting the limits for x and yy
  ax.set_xlim(0,720)
  ax.set_ylim(-1,1)
  x = np.arange(0,frame)
  #calculating the curve line for the graph
  y = np.sin(x * (np.pi/180))
  ax.plot(x,y, "ro")

def run():
  some_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  print(some_animation)
  plt.show()

run()
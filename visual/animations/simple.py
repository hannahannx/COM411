#importing the modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Making the subplots to animate open
fig, ax = plt.subplots()

#Creating a function to show animation
def animate(frame):
  #Setting the limits for the cooridinates
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  ax.plot(frame,frame,"ro")
  
#Running the whole system
def run():
  #allowing the global varible to be access inside the run() funciton
  global fig 
  #assigning the animation function to a varibel so that it will enable me to print it out 
  some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  print(some_animation)
  plt.show()  

run()
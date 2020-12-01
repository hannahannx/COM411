#importing modules 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#creating the figure
fig, ax = plt.subplots()

#initalising the cooridnates for smalll medium and large square
def init ():
  #empty list
  allSquares = []
  #adding dictionary of plots to the list
  small =  {'x':[3,4,4,3,3], 'y':[3,3,4,4,3]}
  allSquares.append(small)
  medium = {'x':[2,2,5,5,2],'y': [2,5,5,2,2]}
  allSquares.append(medium)
  large = {'x': [0,0,6,6,0],'y':[0,6,6,0,0]}
  allSquares.append(large)
  return allSquares


def animate(frame):
  #calling the previous functions values
  ax.cla()
  everySquare = init()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  index = frame % 3
  ax.plot(everySquare[index]['x'],everySquare[index]['y'])

def run():
  some_animation = animation.FuncAnimation(fig,animate,frames = 3,interval = 1000,init_func = init)
  print(some_animation)
  plt.show()

run()


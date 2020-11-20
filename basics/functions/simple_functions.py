#defined a function
def listen():
  #ASKING FOR USER INPUT
  sound = str(input("Please enter a word tha represents a sound"))
  #PRINTING USER INPUT
  print("That was loud {}!!".format(sound))

def run():
  #CALLING THE FUNCTION LISTEN
  listen()

run()
#deifning the function
def identify():
  #creating the varible 
  word = str(input("Please enter a word representing what you can see."))
  if word == "a large boulder":
    print("It's time to run!")
  else:
    print("We will be fine.")

def run():
  #calling the function
  identify()

run()
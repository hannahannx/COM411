#Creating a function
def search(fileName):
  print("Searching...")
  #Prepareing to open and close the file
  with open(fileName) as file:
    #Going throug each line in the text file
    for line in file:
      print("Looked in {}".format(line.strip()))
      #Sucessfuly printed all of the lines
    print("...Done!")

#Creating a function to run the program
def run():
  search("data/files/txt/locations.txt")

#Running the main program 
run()

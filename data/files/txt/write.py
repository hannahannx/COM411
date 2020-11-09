#Creating a function
def search(fileName):
  print("Searching...",end="")
  #Creating empty lists
  sections = []
  books = []
  #Opening the file 
  with open (fileName) as file:
    #Going through each line of the file
    for line in file:
      if line.startswith("Section"):
        #Takes all the values after the first value in the string and adds it on the sections list
        sections.append(line.split(":")[1].strip())
      else:
        #Adds that value to the list of books
        books.append(line.strip())
    print("Done!")
    #Creating a tuple from the sections and the books 
    return sections, books

  
#Creating a function
def save (fileName,storedTuple):
  print("Saving...",end="")
  with open (fileName, "w" ) as file:
      file.write("Sections: {}".format(storedTuple[0]))
      file.write("Books: {}".format(storedTuple[1]))
  print("Done!")

#Creating a function to run the main program
def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt",data)

#Runnning the main program
run()
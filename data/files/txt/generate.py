#Creating a function
def search(fileName):
  print("Searching...",end="")
  #Creating empty lists
  data = {}
  #Opening the file 
  with open (fileName) as file:
    sectionName = ""
    #Going through each line of the file
    for line in file:
      if line.startswith("Section"):
        #Takes all the values after the first value in the string and adds it on the sections list
        sectionName = (line.split(":")[1]).strip()
      elif (sectionName in data):
        data[sectionName].append(line.strip())
      else:
        data[sectionName] = [line.strip()]
    
    print("Done!")
    return data

def run():
  data = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write("{},{}\n".format(section,book))

run()
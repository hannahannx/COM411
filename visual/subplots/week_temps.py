#importing modules
import csv
import matplotlib.pyplot as plt

week1= None
week2= None

#creating a function
def read_data():
  global week1,week2
  with open ("visual/subplots/temps.csv") as csvFile:
    csv_reader = csv.reader(csvFile)
    #igoring the headings (fetch the next row)
    header = next(csv_reader)
    #setting up the data frame
    week1 = header[0].strip()
    week2 = header[1].strip()

    dictionary = {
      week1:[],
      week2:[]
      }
    #every row has 2 values in the list
    for row in csv_reader:
      dictionary[week1].append(row[0].strip())
      dictionary[week2].append(row[1].strip())
  return dictionary

def run():
  data = read_data()
  #vertically placed one abouve the other
  fig, (axes1, axes2) = plt.subplots(2,1,sharex = 'all')
  #drawing to each one
  axes1.plot(data[week1])
  axes2.plot(data[week2])

  plt.show()

run()

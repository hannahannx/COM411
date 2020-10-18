#Creating user inut for the rows and the columns 
rows = int(input("How many rows should I have? "))
columns = int(input("How may columns should I have? "))
#Writing the print statement 
print("Here I go:")
#Creating the rows
for repeats in range(0,rows,1):
  #Creating the columns
  for lines in range(0,columns, 1):
    print(":-)",end="")
  #Creating a new line for the smiley face
  print()
#Printing ending messagefor compilition 
print("Done!")
#Creating varible to ask what the user heard and saw
heard = str(input("What did I hear?"))
see = str(input("What did I see?"))

#Creatin the branches on the responses on what the user heard and Saw
if (heard == "grr") and (see == "two red eyes"):
  print("There is a scary creature. I should get out of here!")
else:
  print("I am a little scared but I will continue.")
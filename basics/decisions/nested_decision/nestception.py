#Creating the location varible so that the uers can respond
location = str(input("Where should I look?"))

if location == "in the bedroom":
  bedroom_location = str(input( "Where in the bedroom should I look?"))
  if bedroom_location == "under the bed":
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")
elif location == "in the bathroom":
  bathroom_location = str(input( "Where in the bathroom should I look?"))
  if bathroom_location == "in the bathtub":
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")
elif location == "in the lab":
  lab_location = str(input( "Where in the lab should I look?"))
  if lab_location == "on the table":
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")
  
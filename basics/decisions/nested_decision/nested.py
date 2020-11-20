def run():
  #Creating the variables
  cover_type = str(input("What type of cover does the book have?"))

  #deciding what type of cover it is and what response it will give out
  if cover_type == "soft":
    shape = str(input("Is the book perfect-bound?"))
    if shape == "yes":
      print("Soft cover, perfect bound books are very popular!")
    else:
      print("Soft covers with coils or stitches are great for short books")
  else:
    print("Books with hard covers can be more expensive!")
  

run()

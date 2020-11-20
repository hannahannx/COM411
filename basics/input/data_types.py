def run ():
  name = str(input("What is your name human?"))
  age = int(input("How old are you (in years)?"))
  height = float(input("How tall are you (in meters"))
  weight = float(input("How much do you weigh in kilograms?"))

  bmi = weight / (height**2)

  print(name,"you are",age,"years old and your bmi is ",bmi)

run()
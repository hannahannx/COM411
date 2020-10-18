#Creating user input and beginning print
phrase = str(input("What phrase do you see? "))
print()
print("Reversing...")
print()
print("The phrase is ",end = "")

reversed = ""
#creating the loop to print backwards(reversed)
for letter in phrase:
  reversed = letter + reversed 
print(reversed)

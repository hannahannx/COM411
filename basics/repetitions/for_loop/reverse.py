#Creating user input and beginning print
phrase = str(input("What phrase do you see? "))
print()
print("Reversing...")
print()
<<<<<<< HEAD
print("The phrase is ",end = "")
#creating the loop to print backwards(reversed)
for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")
=======
#creating the loop to print backwards(reversed)


for reverse in range(-1,len(phrase),1):
  reversed = (phrase[reverse] + (phrase[reverse] + 1))
print(format([reverse]))
>>>>>>> 6b51284992fa6b53057713eec7166b75db4a752f

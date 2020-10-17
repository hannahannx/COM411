#Creating user input and beginning print
phrase = str(input("What phrase do you see? "))
print()
print("Reversing...")
print()
#creating the loop to print backwards(reversed)


for reverse in range(-1,len(phrase),1):
  reversed = (phrase[reverse] + (phrase[reverse] + 1))
print(format([reverse]))
